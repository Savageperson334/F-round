// nextSun
//
// Copied verbatim from https://github.com/hazymorning/origami_weather
//   file src/layout-presets.js, line 10
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const nextSun = (rising) => ({ entity: 'sun.sun', attribute: rising ? 'next_rising' : 'next_setting', visibility: [{ condition: 'state', entity: 'sun.sun', state: rising ? 'below_horizon' : 'above_horizon' }] });
