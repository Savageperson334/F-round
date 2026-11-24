// scaleBarAu
//
// Copied verbatim from https://github.com/Chienlin1014/Orrery
//   file orrery.js, line 212
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function scaleBarAu(scaleAu) {
  const target = scaleAu / 3;
  const steps = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20];
  let chosen = steps[0];
  for (const step of steps) {
    if (step <= target) chosen = step;
  }
  return chosen;
}
