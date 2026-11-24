// event
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 213
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const event = (id, name, group) => ({ id, name, group, kind: 'event', defaultValue: 0, options: null });
