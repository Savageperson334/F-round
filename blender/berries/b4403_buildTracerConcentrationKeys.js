// buildTracerConcentrationKeys
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/simulation/local/tracer.js, line 34
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const BRANCH_TRACER_SUFFIXES = ['_A', '_B']

const TRACER_PREFIX = '__PROD__'


const safeId = (id) => String(id).replace(/[^A-Za-z0-9_]/g, '_')


const buildTracerSpeciesName = (reaction, index) =>
  reaction?.id != null
    ? `${TRACER_PREFIX}RXN_${safeId(reaction.id)}`
    : `${TRACER_PREFIX}RXN_${index}`


const buildTracerConcentrationKeys = (reaction, index) => {
  const base = buildTracerSpeciesName(reaction, index)
  return [base, ...BRANCH_TRACER_SUFFIXES.map((suffix) => `${base}${suffix}`)].map(
    (name) => `CONC.${name}.mol m-3`
  )
}
