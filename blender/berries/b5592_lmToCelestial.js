// lmToCelestial
//
// Copied verbatim from https://github.com/ovro-lwa/astrowidget
//   file js/projection.js, line 204
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function lmToCelestial(l, m, ra0, dec0) {
  const r = Math.sqrt(l * l + m * m);
  if (r > 1.0) return null;

  const sinDec0 = Math.sin(dec0);
  const cosDec0 = Math.cos(dec0);

  let dec, ra;
  if (r === 0) {
    dec = dec0;
    ra = ra0;
  } else {
    const cosc = Math.sqrt(1 - r * r); // cos(angular distance) for SIN
    dec = Math.asin(cosc * sinDec0 + m * cosDec0 / r * r);

    // More numerically stable formulation
    const sinc = r; // sin(angular distance) for SIN where theta = acos(r)
    dec = Math.asin(cosc * sinDec0 + (m * cosDec0 * sinc) / r);
    ra = ra0 + Math.atan2(l * sinc, r * cosDec0 * cosc - m * sinDec0 * sinc);
  }

  return { ra, dec };
}
