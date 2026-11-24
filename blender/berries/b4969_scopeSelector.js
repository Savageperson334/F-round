// scopeSelector
//
// Copied verbatim from https://github.com/elliott-json-park/obsidian-vault-orrery
//   file scripts/build-engine.mjs, line 99
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
