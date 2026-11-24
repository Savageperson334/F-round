// findOrAddPhase
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/redux/slices/mechanismSlice.js, line 25
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const findOrAddPhase = (mechanism, name) => {
  mechanism.phases ??= []
  if (!mechanism.phases.some((phase) => phase.name === name)) {
    mechanism.phases.push({ name, species: [] })
  }
  return mechanism.phases.find((phase) => phase.name === name)
}
