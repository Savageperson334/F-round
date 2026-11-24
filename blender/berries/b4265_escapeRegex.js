// escapeRegex
//
// Copied verbatim from https://github.com/JudahShmoo/BrailleWebTranslatorExtension
//   file brailleMapGenerator.js, line 1
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Braille and tactile information
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
