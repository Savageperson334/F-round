// scalingFactor
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/components/Mechanism/reactions/reactionRegistry.js, line 15
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const scalingFactor = (target) => ({
  key: 'scaling factor',
  placeholder: '1.0',
  name: 'Scaling factor',
  description: `A constant scaling factor for the ${target}.`,
  unit: 'unitless',
})
