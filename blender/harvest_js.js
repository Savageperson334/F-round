// Harvest real, self-contained JavaScript functions from the fetched repositories.
//
// The JavaScript half of harvest.py, with the same rule: every .js file under
// blender/_berries/ is read as TEXT and parsed (never run), and a top-level
// function is kept only when it is pure calculation: it uses nothing but its
// own arguments, a short list of harmless built-ins (Math, JSON, String ...),
// constants of its own file, and other functions of its own file that pass the
// same test. No `this`, no classes, no async, no eval, no `constructor` or
// `prototype`, no assigning to anything outside itself.
//
// Files that look like somebody else's library dropped into the repository
// (lib/ and vendor/ folders, well-known library names, a licence banner at the
// top) are skipped: they are not under the repository's own licence.
//
// Run by harvest.py:  node blender/harvest_js.js <berries folder> <output json>
// Needs acorn:        npm install acorn   (in blender/_work/node)
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { createRequire } = require('module');
const acorn = createRequire(path.join(__dirname, '_work', 'node', 'package.json'))('acorn');

const BERRIES = process.argv[2];
const OUT = process.argv[3];

const GLOBALS = new Set(['Math', 'JSON', 'Number', 'String', 'Boolean', 'Array', 'Object', 'parseInt', 'parseFloat',
  'isNaN', 'isFinite', 'Infinity', 'NaN', 'undefined', 'Map', 'Set', 'Error', 'TypeError', 'RangeError', 'RegExp',
  'encodeURIComponent', 'decodeURIComponent', 'encodeURI', 'decodeURI', 'console']);
const NEW_OK = new Set(['Array', 'Map', 'Set', 'Error', 'TypeError', 'RangeError', 'RegExp', 'Object', 'String', 'Number']);
const DENY_PROPS = new Set(['constructor', 'prototype', 'caller', 'callee', 'defineProperty', 'defineProperties',
  'setPrototypeOf', 'getPrototypeOf', 'getOwnPropertyDescriptor', 'getOwnPropertyDescriptors', 'bind', 'raw']);
const ALLOWED = new Set(['FunctionDeclaration', 'FunctionExpression', 'ArrowFunctionExpression', 'BlockStatement',
  'ReturnStatement', 'IfStatement', 'ForStatement', 'ForOfStatement', 'ForInStatement', 'WhileStatement',
  'DoWhileStatement', 'BreakStatement', 'ContinueStatement', 'VariableDeclaration', 'VariableDeclarator',
  'ExpressionStatement', 'AssignmentExpression', 'UpdateExpression', 'BinaryExpression', 'LogicalExpression',
  'UnaryExpression', 'ConditionalExpression', 'CallExpression', 'MemberExpression', 'Identifier', 'Literal',
  'TemplateLiteral', 'TemplateElement', 'ArrayExpression', 'ObjectExpression', 'Property', 'SpreadElement',
  'SwitchStatement', 'SwitchCase', 'ThrowStatement', 'TryStatement', 'CatchClause', 'NewExpression',
  'SequenceExpression', 'EmptyStatement', 'ChainExpression', 'LabeledStatement', 'ParenthesizedExpression']);
const SKIP_DIRS = new Set(['test', 'tests', '__tests__', 'spec', 'specs', 'docs', 'doc', 'node_modules', 'vendor',
  'vendors', 'dist', 'build', 'lib', 'libs', 'external', 'third_party', 'thirdparty', 'plugins', 'deps', 'bower_components',
  'min', 'minified', 'packages', 'static', 'public', 'assets', 'coverage', 'examples_libs']);
const LIBRARY_NAME = /^(jquery|three|d3|lodash|underscore|bootstrap|p5|react|vue|angular|moment|chart|plotly|leaflet|popper|socket\.io|babylon|pixi|phaser|tone|math|numeric|gl-matrix|dat\.gui|stats|tween|hammer|ace|codemirror|prism|highlight|katex|mathjax|require|modernizr|backbone|handlebars|mustache|axios|ammo|cannon|matter|box2d|howler|anime|gsap|paper|fabric|two|svg|raphael|snap|processing|ml5|tf|tensorflow|brain|opencv|aframe|cesium|ol|mapbox|turf|papaparse|jszip|pako|filesaver|showdown|marked|dompurify|select2|swiper|quill|zepto|ember|knockout|rx|immutable|ramda|async|bluebird|uuid|crypto-js|sjcl|bn|bignumber|decimal|big|fraction|complex|seedrandom|simplex-noise|perlin|noisejs|delaunay|earcut|poly2tri|clipper|proj4|suncalc|webpack|rollup|babel|gulpfile|gruntfile|karma|jest|eslint|vite|polyfill|shim)([.\-_]|$)/i;
const MAX_BYTES = 300000, MAX_LINES = 120, MAX_PARAMS = 4, MAX_CONST_CHARS = 6000;

// ---------------------------------------------------------------- the test

function newState() {
  return { bad: null, declared: new Set(), refs: new Set(), assigned: new Set() };
}

function bindPattern(p, st) {
  if (!p || st.bad) return;
  switch (p.type) {
    case 'Identifier': st.declared.add(p.name); break;
    case 'AssignmentPattern': bindPattern(p.left, st); visit(p.right, st); break;
    case 'ArrayPattern': p.elements.forEach((e) => bindPattern(e, st)); break;
    case 'ObjectPattern':
      for (const q of p.properties) {
        if (q.type === 'RestElement') bindPattern(q.argument, st);
        else { if (q.computed) visit(q.key, st); bindPattern(q.value, st); }
      }
      break;
    case 'RestElement': bindPattern(p.argument, st); break;
    default: st.bad = 'pattern ' + p.type;
  }
}

function assignTarget(p, st) {
  if (!p || st.bad) return;
  switch (p.type) {
    case 'Identifier': st.assigned.add(p.name); st.refs.add(p.name); break;
    case 'MemberExpression': visit(p, st); break;
    case 'AssignmentPattern': assignTarget(p.left, st); visit(p.right, st); break;
    case 'ArrayPattern': p.elements.forEach((e) => assignTarget(e, st)); break;
    case 'ObjectPattern':
      for (const q of p.properties) {
        if (q.type === 'RestElement') assignTarget(q.argument, st);
        else { if (q.computed) visit(q.key, st); assignTarget(q.value, st); }
      }
      break;
    case 'RestElement': assignTarget(p.argument, st); break;
    case 'ParenthesizedExpression': assignTarget(p.expression, st); break;
    default: st.bad = 'target ' + p.type;
  }
}

function deniedName(name) {
  return DENY_PROPS.has(name) || String(name).startsWith('__');
}

function visit(node, st) {
  if (!node || st.bad) return;
  if (Array.isArray(node)) { node.forEach((n) => visit(n, st)); return; }
  if (!ALLOWED.has(node.type)) { st.bad = node.type; return; }
  switch (node.type) {
    case 'Identifier':
      if (node.name === 'arguments' || node.name.startsWith('__')) { st.bad = 'name ' + node.name; return; }
      st.refs.add(node.name);
      return;
    case 'Literal':
      if (node.bigint !== undefined) st.bad = 'bigint';
      return;
    case 'TemplateElement': case 'EmptyStatement': case 'BreakStatement': case 'ContinueStatement':
      return;
    case 'MemberExpression':
      visit(node.object, st);
      if (node.computed) {
        if (node.property.type === 'Literal' && deniedName(node.property.value)) { st.bad = 'property'; return; }
        visit(node.property, st);
      } else if (node.property.type !== 'Identifier' || deniedName(node.property.name)) {
        st.bad = 'property';
      }
      return;
    case 'Property':
      if (node.kind !== 'init') { st.bad = 'getter or setter'; return; }
      if (node.computed) visit(node.key, st);
      else if (deniedName(node.key.type === 'Identifier' ? node.key.name : node.key.value)) { st.bad = 'property'; return; }
      visit(node.value, st);
      return;
    case 'VariableDeclaration':
      for (const d of node.declarations) { bindPattern(d.id, st); visit(d.init, st); }
      return;
    case 'FunctionDeclaration': case 'FunctionExpression': case 'ArrowFunctionExpression':
      if (node.async || node.generator) { st.bad = 'async or generator'; return; }
      if (node.id) st.declared.add(node.id.name);
      node.params.forEach((p) => bindPattern(p, st));
      visit(node.body, st);
      return;
    case 'CatchClause':
      bindPattern(node.param, st);
      visit(node.body, st);
      return;
    case 'AssignmentExpression':
      assignTarget(node.left, st);
      visit(node.right, st);
      return;
    case 'UpdateExpression':
      assignTarget(node.argument, st);
      return;
    case 'ForInStatement': case 'ForOfStatement':
      if (node.await) { st.bad = 'await'; return; }
      if (node.left.type === 'VariableDeclaration') visit(node.left, st); else assignTarget(node.left, st);
      visit(node.right, st);
      visit(node.body, st);
      return;
    case 'LabeledStatement':
      visit(node.body, st);
      return;
    case 'NewExpression':
      if (node.callee.type !== 'Identifier' || !NEW_OK.has(node.callee.name)) { st.bad = 'new'; return; }
      visit(node.arguments, st);
      return;
    default:
      for (const key of Object.keys(node)) {
        if (key === 'type' || key === 'start' || key === 'end' || key === 'loc') continue;
        const child = node[key];
        if (child && typeof child === 'object' && (Array.isArray(child) || typeof child.type === 'string')) visit(child, st);
      }
  }
}

/** The names a piece of code needs from outside itself, or null if it breaks a rule. */
function freeNames(node) {
  const st = newState();
  visit(node, st);
  if (st.bad) return null;
  for (const name of st.assigned) if (!st.declared.has(name)) return null;   // writes to something outside itself
  return [...st.refs].filter((name) => !st.declared.has(name));
}

function returnsSomething(fn) {
  if (fn.body.type !== 'BlockStatement') return true;
  let found = false;
  (function look(node) {
    if (!node || found || typeof node !== 'object') return;
    if (Array.isArray(node)) { node.forEach(look); return; }
    if (node.type === 'ReturnStatement' && node.argument) { found = true; return; }
    if (node !== fn && /Function/.test(node.type || '')) return;
    for (const key of Object.keys(node)) if (key !== 'loc') look(node[key]);
  })(fn);
  return found;
}

// ------------------------------------------------------------------ a file

function harvestFile(full, rel, berry, out, stats) {
  let source;
  try {
    if (fs.statSync(full).size > MAX_BYTES) return;
    source = fs.readFileSync(full, 'utf8');
  } catch (e) { return; }
  if (/@license|@preserve|copyright\s*(\(c\)|©|\d{4})/i.test(source.slice(0, 800))) { stats.skippedAsLibrary++; return; }
  let tree = null;
  for (const sourceType of ['module', 'script']) {
    try { tree = acorn.parse(source, { ecmaVersion: 'latest', sourceType, locations: true, allowHashBang: true }); break; } catch (e) { tree = null; }
  }
  if (!tree) { stats.unreadable++; return; }
  stats.files++;

  const functions = new Map();   // name -> { fn, statement }
  const constants = new Map();   // name -> { init, statement }
  for (let statement of tree.body) {
    if ((statement.type === 'ExportNamedDeclaration' || statement.type === 'ExportDefaultDeclaration') && statement.declaration) {
      statement = statement.declaration;
    }
    if (statement.type === 'FunctionDeclaration' && statement.id) {
      functions.set(statement.id.name, { fn: statement, statement });
    } else if (statement.type === 'VariableDeclaration' && statement.declarations.length === 1) {
      const d = statement.declarations[0];
      if (d.id.type !== 'Identifier' || !d.init) continue;
      if (d.init.type === 'FunctionExpression' || d.init.type === 'ArrowFunctionExpression') functions.set(d.id.name, { fn: d.init, statement });
      else constants.set(d.id.name, { init: d.init, statement });
    }
  }

  const fnVerdict = new Map(), constVerdict = new Map();
  function judgeConst(name, trail) {
    if (constVerdict.has(name)) return constVerdict.get(name);
    let verdict = false;
    const c = constants.get(name);
    if (c && !trail.includes(name) && c.statement.end - c.statement.start <= MAX_CONST_CHARS) {
      const free = freeNames(c.init);
      if (free) {
        const needs = [];
        let ok = true;
        for (const f of free) {
          if (GLOBALS.has(f)) continue;
          if (constants.has(f) && judgeConst(f, trail.concat(name))) needs.push(f); else { ok = false; break; }
        }
        if (ok) verdict = { consts: needs };
      }
    }
    constVerdict.set(name, verdict);
    return verdict;
  }
  function judgeFn(name) {
    if (fnVerdict.has(name)) return fnVerdict.get(name) === null ? { deps: [], consts: [] } : fnVerdict.get(name);
    const entry = functions.get(name);
    if (!entry) return false;
    fnVerdict.set(name, null);
    let verdict = false;
    const free = freeNames(entry.fn);
    if (free) {
      const deps = [], consts = [];
      let ok = true;
      for (const f of free) {
        if (f === name) continue;
        if (functions.has(f)) { if (judgeFn(f)) deps.push(f); else { ok = false; break; } }
        else if (GLOBALS.has(f)) continue;
        else if (judgeConst(f, [])) consts.push(f);
        else { ok = false; break; }
      }
      if (ok) verdict = { deps, consts };
    }
    fnVerdict.set(name, verdict);
    return verdict;
  }
  function closure(name) {
    const consts = [], helpers = [], seenFn = new Set(), seenConst = new Set();
    const addConst = (c) => {
      if (seenConst.has(c)) return;
      seenConst.add(c);
      constVerdict.get(c).consts.forEach(addConst);
      consts.push(c);
    };
    const addFn = (f, root) => {
      if (seenFn.has(f)) return;
      seenFn.add(f);
      const v = fnVerdict.get(f);
      v.consts.forEach(addConst);
      v.deps.forEach((d) => addFn(d, false));
      if (!root) helpers.push(f);
    };
    addFn(name, true);
    return { consts, helpers };
  }
  const text = (statement) => source.slice(statement.start, statement.end);

  for (const [name, entry] of functions) {
    stats.seen++;
    if (name.startsWith('_') || name.startsWith('$') || /^(test|main$|setup$|draw$|init$)/i.test(name)) continue;
    const fn = entry.fn;
    let required = 0, simple = true;
    for (const p of fn.params) {
      if (p.type === 'Identifier') { if (required !== fn.params.indexOf(p)) simple = false; required++; }
      else if (p.type === 'AssignmentPattern' && p.left.type === 'Identifier' && p.right.type === 'Literal') { /* optional */ }
      else simple = false;
    }
    if (!simple || required < 1 || required > MAX_PARAMS || fn.params.length > MAX_PARAMS + 3) continue;
    const lines = entry.statement.loc.end.line - entry.statement.loc.start.line + 1;
    const code = text(entry.statement);
    if (lines > MAX_LINES || code.length < 40 || !returnsSomething(fn)) continue;
    if (!judgeFn(name)) continue;
    const { consts, helpers } = closure(name);
    out.push({
      lang: 'js', repo: berry.repo, shelf: berry.shelf, licence: berry.licence, url: berry.url,
      file: rel.split(path.sep).join('/'), line: entry.statement.loc.start.line, name,
      params: fn.params.map((p) => (p.type === 'Identifier' ? p.name : p.left.name)), required, doc: '',
      source: code, imports: [],
      consts: consts.map((c) => ({ name: c, source: text(constants.get(c).statement) })),
      helpers: helpers.map((h) => ({ name: h, source: text(functions.get(h).statement) })),
      body_print: crypto.createHash('md5').update(source.slice(fn.body.start, fn.body.end).replace(/\s+/g, ' ')).digest('hex'),
    });
    stats.kept++;
  }
}

function walkFolder(base, dir, berry, out, stats) {
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch (e) { return; }
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    const low = entry.name.toLowerCase();
    if (entry.isDirectory()) {
      if (!SKIP_DIRS.has(low) && !low.startsWith('.')) walkFolder(base, full, berry, out, stats);
    } else if (/\.(js|mjs|cjs)$/.test(low) && !/\.(test|spec|config|min)\.[cm]?js$/.test(low) && !LIBRARY_NAME.test(low)) {
      harvestFile(full, path.relative(base, full), berry, out, stats);
    }
  }
}

const stats = { repositories: 0, files: 0, unreadable: 0, skippedAsLibrary: 0, seen: 0, kept: 0 };
const out = [];
for (const folder of fs.readdirSync(BERRIES).sort()) {
  const meta = path.join(BERRIES, folder, '_berry.json');
  if (!fs.existsSync(meta)) continue;
  const berry = JSON.parse(fs.readFileSync(meta, 'utf8'));
  stats.repositories++;
  walkFolder(path.join(BERRIES, folder), path.join(BERRIES, folder), berry, out, stats);
}
fs.writeFileSync(OUT, JSON.stringify({ stats, functions: out }));
console.log(JSON.stringify(stats));
