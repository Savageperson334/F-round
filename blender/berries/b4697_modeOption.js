// modeOption
//
// Copied verbatim from https://github.com/YaseenHQ/Shipwreck
//   file scripts/mock-agent-v2.js, line 16
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Shipwrecks and maritime ghosts
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const modeOption = (current) => ({
  configId: "mode", name: "Mode", type: "select", category: "mode", currentValue: current,
  options: [{ value: "ask", name: "Ask" }, { value: "code", name: "Code" }],
});
