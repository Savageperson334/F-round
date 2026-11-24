// describeStaleInstall
//
// Copied verbatim from https://github.com/MoneyPack/Orrery
//   file theia-app/scripts/smoke-freshness.mjs, line 72
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function describeStaleInstall(stale) {
  const shown = stale.slice(0, 10).map(entry => `  ${entry.file} (${entry.reason})`).join("\n");
  const more = stale.length > 10 ? `\n  ...and ${stale.length - 10} more` : "";
  return [
    `The installed extension copy is stale in ${stale.length} file(s), so the bundle would not`,
    "contain the current extension code and this smoke would certify code that is not running:",
    shown + more,
    "",
    "Run `npm run theia-app:install` after `npm run theia:build`, then re-run the smoke.",
  ].join("\n");
}
