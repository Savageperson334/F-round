// sameIdentity
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/fm1flash.js, line 89
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function sameIdentity(reported, expected) {
  if (!reported || !expected) return false;
  if (reported === expected) return true;
  const r = /^(.+)_(\d{3,})$/.exec(reported), e = /^(.+)_(\d+)$/.exec(expected);
  return !!(r && e && r[1] === e[1] && e[2].length > r[2].length && e[2].startsWith(r[2]));
}
