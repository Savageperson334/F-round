// toThree
//
// Copied verbatim from https://github.com/dsuarezv/satellite-tracker
//   file tle.js, line 51
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const toThree = (v) => {
    return { x: v.x, y: v.z, z: -v.y };
}
