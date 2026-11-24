// getInitialPose
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file demo/camera.js, line 451
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function getInitialPose(startPose, state, rotationOrder) {
    if (!state) return startPose;
    return {
        position: state.position || startPose.position,
        rotation: state.rotation || startPose.rotation,
        rotationOrder: state.rotationOrder || rotationOrder,
        target: state.rotation ? null : startPose.target,
    };
}
