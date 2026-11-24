// paddedTimeDomain
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/components/Plots/chartTicks.js, line 99
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function paddedTimeDomain(times) {
  const finite = times.filter((t) => isFinite(t))
  if (finite.length === 0) return [0, 1]

  const minTime = Math.min(...finite)
  const maxTime = Math.max(...finite)
  if (minTime === maxTime) return [Math.max(0, minTime - 1), maxTime + 1]

  const padding = (maxTime - minTime) * 0.05
  return [Math.max(0, minTime - padding), maxTime + padding]
}
