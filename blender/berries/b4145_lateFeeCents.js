// lateFeeCents
//
// Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
//   file legacy_library/server.js, line 90
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Archaeology & digital heritage
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const GRACE_DAYS = 2;

const CENTS_PER_LATE_DAY = 25;

const FEE_CAP_CENTS = 1000;


function lateFeeCents(daysLate) {
  if (daysLate <= GRACE_DAYS) return 0;
  return Math.min(CENTS_PER_LATE_DAY * daysLate, FEE_CAP_CENTS);
}
