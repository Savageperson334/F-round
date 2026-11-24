// getResultSpeciesNames
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/components/Plots/speciesFormat.js, line 8
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function getSpeciesDisplayName(species) {
  return species.replace(/^CONC\./, '').replace(/\.mol m-3$/, '')
}


function getResultSpeciesNames(results) {
  if (!Array.isArray(results) || results.length === 0) return []
  const firstPoint = results[0]
  const keys =
    firstPoint?.concentrations && typeof firstPoint.concentrations === 'object'
      ? Object.keys(firstPoint.concentrations)
      : Object.keys(firstPoint).filter(
          (key) =>
            key !== 'time' && key !== 'timestamp' && key !== 'date' && key !== 'concentrations'
        )
  return keys.map(getSpeciesDisplayName)
}
