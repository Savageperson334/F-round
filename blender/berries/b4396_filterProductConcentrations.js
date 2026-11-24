// filterProductConcentrations
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/simulation/local/run.js, line 61
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const filterProductConcentrations = (results, excludeConcentrationKeys) => {
  const excludeSet = new Set(excludeConcentrationKeys)
  const filteredResults = []
  const excludedResults = []

  for (const point of results) {
    if (!point || typeof point !== 'object' || !point.concentrations) {
      filteredResults.push(point)
      excludedResults.push({})
      continue
    }

    const filteredConcentrations = {}
    const excludedConcentrations = {}

    for (const [key, value] of Object.entries(point.concentrations)) {
      if (excludeSet.has(key)) {
        excludedConcentrations[key] = value
      } else {
        filteredConcentrations[key] = value
      }
    }

    filteredResults.push({ ...point, concentrations: filteredConcentrations })
    excludedResults.push({
      time: point.time,
      concentrations: excludedConcentrations,
      environment: point.environment,
    })
  }

  return {
    filteredResults,
    excludedResults,
  }
}
