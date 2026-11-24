// preserveMaterialShaderHooks
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/tint.js, line 38
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function preserveMaterialShaderHooks(source, clone) {
    if (typeof source.onBeforeCompile === 'function') {
        clone.onBeforeCompile = source.onBeforeCompile;
    }
    if (typeof source.customProgramCacheKey === 'function') {
        clone.customProgramCacheKey = source.customProgramCacheKey;
    }
    return clone;
}
