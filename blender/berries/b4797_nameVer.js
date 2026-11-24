// nameVer
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/fwcards.js, line 139
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const shortVer = (v) => String(v).replace(/^[A-Za-z][A-Za-z0-9]*-(?=v?\d)/, "");


function nameVer(name, version) {
  const v = shortVer(String(version || "").trim());
  if (!v || name.toLowerCase().endsWith(v.toLowerCase())) return name;
  if (/^V\d+$/i.test(v) && /\sV\d+$/i.test(name)) return name.replace(/V\d+$/i, v.toUpperCase());
  return `${name} ${v}`;
}
