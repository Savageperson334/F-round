// fmt
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/studio.js, line 6
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fmt(t){const m=Math.floor(t/60),s=Math.floor(t%60),ms=Math.floor(t%1*1000);return`${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}.${String(ms).padStart(3,'0')}`}
