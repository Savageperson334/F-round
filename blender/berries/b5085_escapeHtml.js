// escapeHtml
//
// Copied verbatim from https://github.com/hazymorning/origami_weather
//   file src/origami-weather.js, line 1477
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ESCAPE_MAP = { '&': '&amp;', '"': '&quot;', '<': '&lt;', '>': '&gt;' };


const escapeHtml = (v) => String(v).replace(/["&<>]/g, c => ESCAPE_MAP[c]);
