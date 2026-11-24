// normalizeType
//
// Copied verbatim from https://github.com/pshenok/server-survival
//   file src/ui/toolbar.js, line 257
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function normalizeType(type) {
    return type === "lambda" ? "compute" : type;
}
