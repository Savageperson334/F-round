// changelogUrl
//
// Copied verbatim from https://github.com/weenas/castbay
//   file desktop/app/ui/app.js, line 518
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

let lang = "en";


function changelogUrl(version) {
  return `https://castbay.weenas.com/${lang === "zh" ? "zh/" : ""}changelog#desktop-v${version}`;
}
