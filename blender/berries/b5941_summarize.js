// summarize
//
// Copied verbatim from https://github.com/sn3p/Orrery3D
//   file benchmarks/browser.js, line 11
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const percentile = (values, p) => {
  const a = [...values].sort((a, b) => a - b);
  return a.length ? a[Math.min(a.length - 1, Math.floor(a.length * p))] : null;
};


const summarize = values => ({ median: percentile(values, 0.5), p95: percentile(values, 0.95) });
