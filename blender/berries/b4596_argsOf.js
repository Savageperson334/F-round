// argsOf
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/tools/shared.mjs, line 9
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function argsOf(argv) { return Object.fromEntries(argv.map(v => { const [k,...rest] = v.replace(/^--/,'').split('='); return [k, rest.length ? rest.join('=') : true]; })); }
