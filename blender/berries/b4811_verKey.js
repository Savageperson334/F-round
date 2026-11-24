// verKey
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/fwcards.js, line 293
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const normVer = (v) => String(v || "").trim().replace(/^v/i, "").toLowerCase();


const shortVer = (v) => String(v).replace(/^[A-Za-z][A-Za-z0-9]*-(?=v?\d)/, "");


function verKey(v) {
  const s = String(v || "").trim().toLowerCase();
  const m = s.match(/(\d+(?:\.\d+)+)(.*)$/);
  if (!m) return normVer(shortVer(s));
  return m[1].replace(/(\.0+)+$/, "") + m[2].replace(/[\s()[\]]/g, "");
}
