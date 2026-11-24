// generateCanonicalUrl
//
// Copied verbatim from https://github.com/Archeb/opentrace
//   file HomePage/build.js, line 92
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function generateCanonicalUrl(baseUrl, langPath) {
    return langPath ? `${baseUrl}/${langPath}/` : `${baseUrl}/`;
}
