// cleanName
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/wavetable.js, line 230
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const WT = {
  FRAMES: 19, HARMONICS: 64, BYTES: 19 * 64, NAME: 8, SLOTS: 3, HDR: 12, OBJ: 12 + 19 * 64, VERSION: 1,
  FIRST_TABLE: 26,                 // TABLE value of USR1 (the 26 factory tables come first)
  CMD: { LIST: 81, GET: 82, PUT: 83 }, BACKUP_IDS: [24, 25, 26], CAPS_BIT: 8,   // INFO 42 01 caps bit 3
  CHUNK: 112,                      // bytes of table data a GET / PUT piece carries (16 pack7 groups)
};


function cleanName(s) { return String(s ?? "").toUpperCase().replace(/[^A-Z0-9 .+#-]/g, "").replace(/ +/g, " ").trim().slice(0, WT.NAME).trim(); }
