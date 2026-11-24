// cloneSettings
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/operation/settings.js, line 20
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function normalizeValue(value) {
  if (value && typeof value.getHexString === "function") {
    return `#${value.getHexString()}`;
  }
  if (Array.isArray(value)) {
    return value.map((item) => normalizeValue(item));
  }
  if (value && typeof value === "object") {
    const result = {};
    Object.entries(value).forEach(([key, item]) => {
      result[key] = normalizeValue(item);
    });
    return result;
  }
  return value;
}


function cloneSettings(value) {
  return normalizeValue(value);
}
