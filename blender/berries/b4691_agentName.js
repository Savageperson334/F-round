// agentName
//
// Copied verbatim from https://github.com/YaseenHQ/Shipwreck
//   file scripts/handoff-check.js, line 16
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Shipwrecks and maritime ghosts
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const agentName = (id) => ({ a1: "Echo A", a2: "Echo B", a3: "Devin" }[id] ?? id);
