// freqLabel
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/dx7.js, line 114
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function freqLabel(mode, coarse, fine) {
  if (mode === 1) {
    const hz = Math.pow(10, coarse % 4) * Math.exp((Math.LN10 * fine) / 100);
    return hz >= 1000 ? `${(hz / 1000).toFixed(2)} kHz` : `${hz.toFixed(hz < 10 ? 3 : 1)} Hz`;
  }
  const base = coarse === 0 ? 0.5 : coarse;
  return `×${(base * (1 + fine / 100)).toFixed(2)}`;
}
