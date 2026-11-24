// mapEdsmTerraformState
//
// Copied verbatim from https://github.com/TerjeRu/orrery
//   file shared/src/edsm-mapping.js, line 51
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function mapEdsmTerraformState(terraformingState) {
  if (!terraformingState || terraformingState === 'Not terraformable') return '';
  return terraformingState;
}
