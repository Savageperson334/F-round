// Elliptic
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 423
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const kPi = 3.14159265358979323846;


const clamp = (v, lo, hi) => (v < lo ? lo : hi < v ? hi : v);


function Elliptic(m) {
  m = clamp(m, 0.0, 1.0 - 1e-16);
  let a = 1.0;
  let b = Math.sqrt(1.0 - m);
  let sum = 0.5 * m;
  let power = 0.5;
  for (let i = 0; i < 64; i += 1) {
    const c = 0.5 * (a - b);
    const an = 0.5 * (a + b);
    b = Math.sqrt(a * b);
    a = an;
    power *= 2.0;
    const term = power * c * c;
    sum += term;
    if (term <= 1e-17 * sum) break;
  }
  const K = kPi / (2.0 * a);
  return { K, E: K * (1.0 - sum) };
}
