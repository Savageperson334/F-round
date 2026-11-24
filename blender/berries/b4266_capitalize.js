// capitalize
//
// Copied verbatim from https://github.com/JudahShmoo/BrailleWebTranslatorExtension
//   file content.js, line 262
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Braille and tactile information
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function capitalize(text) {
    text = text.replace(/\b[A-Z]{2,}\b/gm, (match) => `⠠⠠${match.toLowerCase()}`);
    return text.replace(/[A-Z]/gm, `⠠$&`).toLowerCase();
}
