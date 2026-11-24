// checkControlValue
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/detectors.js, line 130
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function checkControlValue(object, key, schema, value) {
  if (value === undefined) {
    return { severity: 'info', code: 'UNSET_CONTROL', message: `${object.id}.${key} has no value`, frame: object.id };
  }
  if (schema === 'text' && typeof value !== 'string') {
    return { severity: 'error', code: 'CONTROL_TYPE', message: `${object.id}.${key} must be text`, frame: object.id };
  }
  if (schema === 'color' && !(typeof value === 'string' && /^#[0-9a-f]{6}$/i.test(value))) {
    return { severity: 'error', code: 'CONTROL_COLOR', message: `${object.id}.${key} must be a hex color`, frame: object.id };
  }
  if (Array.isArray(schema) && typeof schema[0] === 'string') {
    if (typeof value !== 'string' || !schema.includes(value)) {
      return { severity: 'error', code: 'CONTROL_OPTION', message: `${object.id}.${key} is not an allowed option`, frame: object.id };
    }
  }
  if (Array.isArray(schema) && typeof schema[0] === 'number') {
    const [min, max] = schema;
    if (typeof value !== 'number' || !Number.isFinite(value)) {
      return { severity: 'error', code: 'CONTROL_TYPE', message: `${object.id}.${key} must be a number`, frame: object.id };
    }
    if (value < min || value > max) {
      return { severity: 'error', code: 'CONTROL_RANGE', message: `${object.id}.${key}=${value} is outside [${min}, ${max}]`, frame: object.id };
    }
  }
  return null;
}
