// formatBound
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/components/Plots/timeRangeUnits.js, line 16
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const formatBound = (raw, divisor, sigDigits, decimals) => {
  // Non-finite bounds (e.g. an upstream NaN range) would render as "NaN"/"Infinity" and
  // prevent editing. Editable fields need a valid number to resume from.
  if (!Number.isFinite(raw)) return '0'
  const scaled = raw / divisor
  if (sigDigits != null) return String(scaled.toExponential(sigDigits))
  // parseFloat trims trailing zeros from toFixed (e.g. "3.00" -> 3 -> "3") so whole numbers
  // still read cleanly instead of always showing the full decimal precision.
  if (decimals != null) return String(parseFloat(scaled.toFixed(decimals)))
  return String(scaled)
}
