// parseArgs
//
// Copied verbatim from https://github.com/hermetic-modular/alchemy-sdk
//   file tools/hostlink-cli/hostlink.mjs, line 331
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "-p" || a === "--port") args.port = argv[++i];
    else if (a === "--follow") args.follow = true;
    else if (a === "--json") args.json = true;
    else if (a === "--level") args.level = argv[++i];
    else if (a.startsWith("--") && a !== "--help") throw new Error(`Unknown option: ${a}`);
    else args._.push(a);
  }
  return args;
}
