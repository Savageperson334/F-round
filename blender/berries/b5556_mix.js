// mix
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/theme.js, line 9
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rgb = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));


const hex = (c) => "#" + c.map((v) => Math.round(Math.min(255, Math.max(0, v))).toString(16).padStart(2, "0")).join("");


const mix = (a, b, pct) => { const x = rgb(a), y = rgb(b); return hex(x.map((v, i) => v + (y[i] - v) * pct / 100)); };
