// midi
//
// Copied verbatim from https://github.com/jb3/meeple
//   file web/audio/music.js, line 25
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Peculiar interfaces, worlds, visual systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const midi = (n) => 440 * Math.pow(2, (n - 69) / 12);
