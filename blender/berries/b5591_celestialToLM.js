// celestialToLM
//
// Copied verbatim from https://github.com/ovro-lwa/astrowidget
//   file js/projection.js, line 178
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function celestialToLM(ra, dec, ra0, dec0) {
  const dra = ra - ra0;
  const sinDec = Math.sin(dec);
  const cosDec = Math.cos(dec);
  const sinDec0 = Math.sin(dec0);
  const cosDec0 = Math.cos(dec0);
  const cosDra = Math.cos(dra);

  // Visibility check: cos(angular distance) > 0 means on the near side
  const cosc = sinDec * sinDec0 + cosDec * cosDec0 * cosDra;

  const l = cosDec * Math.sin(dra);
  const m = sinDec * cosDec0 - cosDec * sinDec0 * cosDra;

  return { l, m, visible: cosc > 0 };
}
