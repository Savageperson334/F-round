// triad
//
// Copied verbatim from https://github.com/jb3/meeple
//   file web/audio/events.js, line 41
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Peculiar interfaces, worlds, visual systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const TRIAD_Q = { 0: [0, 4, 7], 2: [0, 3, 7], 4: [0, 3, 7], 5: [0, 4, 7], 7: [0, 4, 7], 9: [0, 3, 7], 11: [0, 3, 6] };


const triad = (deg) => TRIAD_Q[deg].map((iv) => deg + iv);
