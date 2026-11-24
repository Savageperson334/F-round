// classifyOrbit
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/catalog/population.js, line 179
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const NEA_PERIHELION_AU = 1.3;

const CLASS_NEA = 1;

const TROJAN_A_MIN = 4.8;

const TROJAN_A_MAX = 5.4;

const TROJAN_E_MAX = 0.3;

const CLASS_TROJAN = 2;

const JUPITER_AU = 5.204;

const CLASS_DISTANT = 3;

const HILDA_A_MIN = 3.7;

const HILDA_A_MAX = 4.2;

const CLASS_HILDA = 7;

const HUNGARIA_A_MAX = 2.0;

const HUNGARIA_I_MIN = 16;

const HUNGARIA_I_MAX = 34;

const HUNGARIA_E_MAX = 0.18;

const CLASS_HUNGARIA = 8;

const BELT_INNER_MAX_AU = 2.5;

const CLASS_BELT_INNER = 4;

const BELT_MIDDLE_MAX_AU = 2.82;

const CLASS_BELT_MIDDLE = 5;

const CLASS_BELT_OUTER = 6;


function classifyOrbit(a, e, i = 0) {
  const q = a * (1 - e);
  if (q < NEA_PERIHELION_AU) return CLASS_NEA;
  if (a > TROJAN_A_MIN && a < TROJAN_A_MAX && e < TROJAN_E_MAX) return CLASS_TROJAN;
  if (a >= JUPITER_AU) return CLASS_DISTANT;
  if (a >= HILDA_A_MIN && a < HILDA_A_MAX) return CLASS_HILDA;
  if (a < HUNGARIA_A_MAX && i >= HUNGARIA_I_MIN && i <= HUNGARIA_I_MAX && e <= HUNGARIA_E_MAX) return CLASS_HUNGARIA;
  if (a < BELT_INNER_MAX_AU) return CLASS_BELT_INNER;
  if (a < BELT_MIDDLE_MAX_AU) return CLASS_BELT_MIDDLE;
  return CLASS_BELT_OUTER;
}
