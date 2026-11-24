// scenarioPreview
//
// Copied verbatim from https://github.com/pshenok/server-survival
//   file src/ui/campaign-ui.js, line 37
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function scenarioPreview(scenario) {
    const chars = [...scenario];
    return chars.length > 80 ? chars.slice(0, 80).join("") + "…" : scenario;
}
