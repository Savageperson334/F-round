// applyReactionComponents
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/components/Mechanism/reactions/reactionUtils.js, line 72
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const parseReactionString = (str) => {
  return str
    .split('+')
    .map((value) => value.trim())
    .filter(Boolean)
    .map((value) => {
      const match = value.match(/^(\d*\.?\d*)\s*(.+)$/)

      if (match) {
        const coeff = match[1] ? parseFloat(match[1]) : 1.0
        return {
          name: match[2].trim(),
          coefficient: coeff,
        }
      }

      return {
        name: value,
        coefficient: 1.0,
      }
    })
}


const parseSide = (text) => {
  const trimmed = String(text ?? '').trim()
  return trimmed === '' || trimmed === '∅' ? [] : parseReactionString(trimmed)
}


function applyReactionComponents(reaction, values, fields) {
  const updated = { ...reaction }
  for (const field of fields) {
    const label = field.label ?? field.key
    const parsed = parseSide(values[field.key])
    if (parsed.length === 0 && field.required) return { error: `${label} cannot be empty.` }
    if (field.single) {
      if (parsed.length > 1) return { error: `${label} must be a single species.` }
      if (parsed.length === 1 && parsed[0].coefficient !== 1) {
        return { error: `${label} cannot have a coefficient.` }
      }
      updated[field.key] = parsed[0]?.name ?? ''
    } else {
      updated[field.key] = parsed
    }
  }
  return { reaction: updated }
}
