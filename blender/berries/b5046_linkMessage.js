// linkMessage
//
// Copied verbatim from https://github.com/forkwiki/fork
//   file netlify/functions/season.mjs, line 34
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Archaeology, caves, museums, archival fragments
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const linkMessage = (handle, wallet, issued) =>
  `forks.wiki · Season 0\n\nLink this wallet to @${handle} on forks.wiki, so the coins it launches earn $FORK.\n\nWallet: ${wallet}\nIssued: ${issued}\n\nSigning is free and moves no funds.`;
