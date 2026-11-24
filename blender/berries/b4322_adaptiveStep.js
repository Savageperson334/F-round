// adaptiveStep
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/components/Plots/chartTicks.js, line 12
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const clean = (value) => Number(value.toPrecision(12))


function adaptiveStep(rough, correction = 0) {
  if (!(rough > 0)) return 0
  const digitCount = Math.floor(Math.log10(rough)) + 1
  const magnitude = 10 ** digitCount
  const ratioStep = digitCount !== 1 ? 0.05 : 0.1
  return clean(
    (Math.ceil(clean(rough / magnitude / ratioStep)) + correction) * ratioStep * magnitude
  )
}
