// eccentricAnomaly
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/pixi/Orbit.js, line 24
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//   the same function also appears in: sn3p/Orrery3D
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const TAU = 2 * Math.PI;


function eccentricAnomaly(mean, e) {
  // Signed wrapping preserves small negative phases without adding a full turn.
  let M = mean % TAU;
  if (M > Math.PI) M -= TAU;
  if (M < -Math.PI) M += TAU;
  if (M === 0 || e === 0) return M;
  const sign = Math.sign(M);
  M = Math.abs(M);
  let lo = 0, hi = Math.PI;
  let E = e < 0.8 ? M : Math.PI;
  // Kepler's equation is monotonic for 0 <= e < 1. Keep a root bracket
  // throughout Newton iteration; reject steps that leave it.
  for (let i = 0; i < 16; i++) {
    const residual = E - e * Math.sin(E) - M;
    if (residual === 0) return sign * E;
    if (residual > 0) hi = E;
    else lo = E;
    const next = E - residual / (1 - e * Math.cos(E));
    if (!(next > lo && next < hi)) break;
    if (Math.abs(next - E) <= 1e-14) return sign * next;
    E = next;
  }
  // A fixed bisection budget guarantees termination even near e = 1.
  for (let i = 0; i < 64; i++) {
    E = (lo + hi) / 2;
    const residual = E - e * Math.sin(E) - M;
    if (residual === 0 || hi - lo <= 1e-14) break;
    if (residual > 0) hi = E;
    else lo = E;
  }
  return sign * E;
}
