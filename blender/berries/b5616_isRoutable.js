// isRoutable
//
// Copied verbatim from https://github.com/pshenok/server-survival
//   file src/sim/circuit-breaker.js, line 66
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function isRoutable(service) {
    if (!service || service.isDisabled) return false;
    // A GPU loading its model (#87) is unroutable — the one line the AI Wave
    // adds here. modelLoading is a DEDICATED flag, never isDisabled: the
    // event system re-enables disabled services, and using it would let a
    // pause cancel a model load.
    if (service.modelLoading) return false;
    if (service.breakerState === "open") return false;
    if (service.breakerState === "half-open") return service.breakerProbes > 0;
    return true;
}
