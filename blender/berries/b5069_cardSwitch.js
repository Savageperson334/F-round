// cardSwitch
//
// Copied verbatim from https://github.com/hazymorning/origami_weather
//   file src/layout-presets.js, line 9
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const cardSwitch = (name) => ({ tap: { action: 'toggle', entity: `origami.${name}` }, tab: (state) => ({ action: 'toggle', entity: `origami.${name}`, state }), shown: (state) => [{ condition: 'state', entity: `origami.${name}`, state }] });
