// nameFirst
//
// Copied verbatim from https://github.com/hazymorning/origami_weather
//   file src/origami-weather-editor.js, line 35
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const nameFirst = (o) => { const n = typeof o.name === "string" ? o.name.trim() : ""; const { name, ...rest } = o; return n ? { name: n, ...rest } : rest; };
