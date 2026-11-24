// stagedLag
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/motion.js, line 252
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function stagedLag(u, time, beat, lagFactor) {
  // The absolute clock is kept in the signature for call-site parity; the phase
  // is fully described by `beat`, so no frame-to-frame integration is needed.
  void time;
  return lagFactor * u * Math.sin(beat - u * lagFactor);
}
