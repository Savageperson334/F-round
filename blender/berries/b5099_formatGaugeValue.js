// formatGaugeValue
//
// Copied verbatim from https://github.com/hermetic-modular/alchemy-sdk
//   file tools/hostlink-cli/diagnostics-codec.mjs, line 105
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatGaugeValue(value) {
    if (value === null)
        return "No value";
    if (typeof value === "boolean")
        return value ? "Yes" : "No";
    return Number.isInteger(value) ? String(value) : String(Number(value.toPrecision(6)));
}
