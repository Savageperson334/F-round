// mkApp
//
// Copied verbatim from https://github.com/elliott-json-park/obsidian-vault-orrery
//   file scripts/smoke.cjs, line 49
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const mkApp = vault => ({
  vault: Object.assign({ getMarkdownFiles: () => [], getName: () => 'VAULT' }, vault),
  workspace: { on() {}, getLeavesOfType: () => [], getActiveFile: () => null,
               /* run at once: the stub has no layout to wait for, and the
                  first-run sidebar placement is what it is there to check */
               onLayoutReady: f => f(), getRightLeaf: () => null },
  metadataCache: { on() {}, resolvedLinks: {}, unresolvedLinks: {}, getFileCache: () => null },
});
