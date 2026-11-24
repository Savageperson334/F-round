// scopeCss
//
// Copied verbatim from https://github.com/elliott-json-park/obsidian-vault-orrery
//   file scripts/build-engine.mjs, line 118
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const CLS  = 'vo-root';


function scopeSelector(sel) {
  return sel.split(',').map(s => {
    s = s.trim();
    if (!s) return s;
    /* the variable block and the page box all become the root itself */
    if (s === ':root' || s === 'html' || s === 'body' || s === 'html,body') return '.' + CLS;
    /* the reset has to reach the root as well as its descendants */
    if (s === '*') return `.${CLS}, .${CLS} *`;
    /* body.sky and the like are mode flags that the
       engine now toggles on the root */
    if (/^body(?=[.#:\[])/.test(s)) return '.' + CLS + s.slice(4);
    if (/^html(?=[.#:\[])/.test(s)) return '.' + CLS + s.slice(4);
    if (s.startsWith('.' + CLS)) return s;
    return `.${CLS} ${s}`;
  }).join(', ');
}


function scopeCss(input) {
  let out = '', i = 0, buf = '';
  while (i < input.length) {
    const c = input[i];
    if (c === '{') {
      const head = buf.trim();
      buf = '';
      /* find the matching close */
      let depth = 1, j = i + 1;
      while (j < input.length && depth > 0) {
        if (input[j] === '{') depth++;
        else if (input[j] === '}') depth--;
        j++;
      }
      const inner = input.slice(i + 1, j - 1);
      if (/^@(media|supports|container|layer)/i.test(head)) {
        out += head + ' {' + scopeCss(inner) + '}';
      } else if (/^@(keyframes|-webkit-keyframes|font-face|property)/i.test(head)) {
        out += head + ' {' + inner + '}';           // percentages, not selectors
      } else {
        out += scopeSelector(head) + ' {' + inner + '}';
      }
      i = j;
    } else { buf += c; i++; }
  }
  return out + buf;
}
