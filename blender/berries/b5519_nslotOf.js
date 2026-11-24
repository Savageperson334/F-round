// nslotOf
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/patslot.js, line 14
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const PS = { REC: 596, USED: 0xA7, VER: 2, NAME: 12, STEPS: 64, STEP: 9, PER: 11, SLOTS: 32, NOBJ: 3, HDR: 8, OBJ_MAX: 3584, MAGIC: [0x50, 0x54, 0x53, 0x33] };


const nslotOf = (o) => Math.min(PS.PER, PS.SLOTS - o * PS.PER);
