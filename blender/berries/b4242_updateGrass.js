// updateGrass
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/grass.js, line 586
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function updateGrass(grass, time) {
    if (!grass) return grass;
    var material = grass.userData && grass.userData.grassMaterial || grass.material,
        uniforms = material && material.userData && material.userData.grassUniforms;
    if (uniforms) {
        uniforms.time.value = time;
    }
    return grass;
}
