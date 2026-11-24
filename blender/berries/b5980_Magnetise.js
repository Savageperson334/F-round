// Magnetise
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 315
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const kMu0 = 1.25663706212e-6;


const max2 = (a, b) => (a < b ? b : a);


function Langevin(x) {
  const a = Math.abs(x);
  if (a < 1e-2) {
    const x2 = x * x;
    return x * (1.0 / 3.0 - x2 / 45.0 + (2.0 * x2 * x2) / 945.0);
  }
  return 1.0 / Math.tanh(x) - 1.0 / x;
}


const Magnetisation = (fluid, h) => fluid.saturation * Langevin((3.0 * fluid.chi * h) / fluid.saturation);


function LangevinSlope(x) {
  const a = Math.abs(x);
  if (a < 1e-2) {
    const x2 = x * x;
    return 1.0 / 3.0 - x2 / 15.0 + (2.0 * x2 * x2) / 189.0;
  }
  if (a > 350.0) return 1.0 / (x * x);
  const s = Math.sinh(x);
  return 1.0 / (x * x) - 1.0 / (s * s);
}


const Susceptibility = (fluid, h) => 3.0 * fluid.chi * LangevinSlope((3.0 * fluid.chi * h) / fluid.saturation);


function Magnetise(fluid, applied) {
  const op = { applied: max2(applied, 0.0), inside: 0.0, m: 0.0, chord: 1.0, tangent: 1.0, r0: 1.0, g: 0.0 };
  let lo = 0.0;
  let hi = op.applied;
  for (let i = 0; i < 200 && hi - lo > 0.0; i += 1) {
    const mid = 0.5 * (lo + hi);
    if (mid === lo || mid === hi) break;
    if (mid + Magnetisation(fluid, mid) < op.applied) lo = mid;
    else hi = mid;
  }
  op.inside = 0.5 * (lo + hi);
  op.m = Magnetisation(fluid, op.inside);
  op.chord = op.inside > 0.0 ? 1.0 + op.m / op.inside : 1.0 + fluid.chi;
  op.tangent = 1.0 + Susceptibility(fluid, op.inside);
  op.r0 = Math.sqrt(op.chord * op.tangent);
  op.g = kMu0 * op.m * op.m * (op.r0 / (1.0 + op.r0));
  return op;
}
