// rateHeader
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/conditions/rateColumns.js, line 46
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SURFACE_PROPERTIES = [
  { property: 'effective radius', unit: 'm', displayUnit: 'm' },
  { property: 'particle number concentration', unit: '# m-3', displayUnit: 'particles m-3' },
]

const RATE_TYPES = [
  { reactionType: 'PHOTOLYSIS', prefix: 'PHOTO', label: 'Photolysis', unit: 's-1' },
  { reactionType: 'EMISSION', prefix: 'EMIS', label: 'Emission', unit: 'mol m-3 s-1' },
  { reactionType: 'FIRST_ORDER_LOSS', prefix: 'LOSS', label: 'Loss', unit: 's-1' },
  { reactionType: 'USER_DEFINED', prefix: 'USER', label: 'User defined', unit: 's-1' },
  { reactionType: 'SURFACE', prefix: 'SURF', label: 'Surface', unit: null },
]


function rateHeader(prefix, name, property = null) {
  if (prefix === 'SURF') {
    const unit = SURFACE_PROPERTIES.find((p) => p.property === property)?.unit
    return unit ? `SURF.${name}.${property}.${unit}` : `SURF.${name}.${property}`
  }
  const unit = RATE_TYPES.find((type) => type.prefix === prefix)?.unit
  return unit ? `${prefix}.${name}.${unit}` : `${prefix}.${name}`
}
