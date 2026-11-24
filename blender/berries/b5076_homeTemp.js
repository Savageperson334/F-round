// homeTemp
//
// Copied verbatim from https://github.com/hazymorning/origami_weather
//   file src/layout-presets.js, line 225
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const text = (extra) => ({ type: 'text', ...extra });


const homeText = (extra) => text({ weight: '500', color: 'var(--primary-text-color)', ...extra });


const homeTemp = (extra) => homeText({ precision: 0, format: '\u00b0', weight: '700', ...extra });
