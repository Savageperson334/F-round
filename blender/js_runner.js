// Runs harvested JavaScript functions with nothing in reach.
//
// Reads one JSON message per line on stdin and answers with one JSON line:
//   {"load": key, "name": "fn", "code": "..."}   ->  {"ok": true}
//   {"call": key, "args": "[...json...]"}         ->  {"ok": true, "value": "...json..."}
//
// The functions live in one empty vm context: no require, no process, no
// timers, no network. Creating code from strings (eval, Function) is switched
// off there, the built-in prototypes are frozen, and every load and call has a
// time limit. Only text goes in and only text comes out, so nothing from this
// outer program is ever handed to them.
//
// Start it as:  node --permission --allow-fs-read=<this folder> js_runner.js [milliseconds]
'use strict';
const vm = require('vm');
const readline = require('readline');

const TIMEOUT = parseInt(process.argv[2] || '800', 10);

const box = Object.create(null);
const context = vm.createContext(box, { codeGeneration: { strings: false, wasm: false } });
vm.runInContext(`
  var console = { log() {}, warn() {}, error() {}, info() {}, debug() {}, assert() {}, table() {}, trace() {} };
  var __fns = Object.create(null);
  var __args = '', __key = '', __made = undefined;
  for (const name of ['eval', 'Function', 'WebAssembly', 'Reflect', 'Proxy', 'Atomics', 'SharedArrayBuffer',
                      'FinalizationRegistry', 'WeakRef', 'Promise', 'globalThis']) {
    delete this[name];
  }
  for (const thing of [Object, Array, String, Number, Boolean, Math, JSON, Map, Set, Error, Symbol,
                       Object.prototype, Array.prototype, String.prototype, Number.prototype, Boolean.prototype,
                       Map.prototype, Set.prototype, Error.prototype, RegExp.prototype, Symbol.prototype,
                       (function () {}).constructor.prototype]) {
    Object.freeze(thing);
  }
`, context);

const keep = new vm.Script('__fns[__key] = __made; __made = undefined;');
const call = new vm.Script(`(function () {
  var s = JSON.stringify(__fns[__key].apply(undefined, JSON.parse(__args)));
  return typeof s === 'string' ? s : '';
})()`);

function handle(message) {
  // Whatever a borrowed function throws is never looked at: it is only ever "that did not work".
  try {
    if (message.load !== undefined) {
      if (!/^[A-Za-z_$][A-Za-z0-9_$]*$/.test(String(message.name))) return { ok: false };
      box.__made = vm.runInContext('(function () {\n' + message.code + '\n;return ' + message.name + ';\n})()',
        context, { timeout: TIMEOUT });
      if (typeof box.__made !== 'function') return { ok: false };
      box.__key = String(message.load);
      keep.runInContext(context);
      return { ok: true };
    }
    if (message.call !== undefined) {
      box.__key = String(message.call);
      box.__args = String(message.args);
      const out = call.runInContext(context, { timeout: TIMEOUT });
      if (typeof out !== 'string' || out === '' || out.length > 200000) return { ok: false };
      return { ok: true, value: out };
    }
  } catch (error) {
    return { ok: false };
  }
  return { ok: false };
}

const lines = readline.createInterface({ input: process.stdin, crlfDelay: Infinity });
lines.on('line', (line) => {
  let reply = { ok: false };
  try {
    reply = handle(JSON.parse(line));
  } catch (error) {
    reply = { ok: false };
  }
  process.stdout.write(JSON.stringify(reply) + '\n');
});
lines.on('close', () => process.exit(0));
