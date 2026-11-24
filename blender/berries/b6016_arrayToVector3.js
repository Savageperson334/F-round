// arrayToVector3
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/operation/mesh.js, line 157
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function arrayToVector3(data) {
  // change all arrays (position, scale, rotation) inside the data form [0, 0, 0] to {x: 0, y: 0, z: 0}
  // if position exists and is an array, convert it to object
  if (data.position && Array.isArray(data.position)) {
    data.position = { x: data.position[0], y: data.position[1], z: data.position[2] };
  }
  if (data.scale && Array.isArray(data.scale)) {
    data.scale = { x: data.scale[0], y: data.scale[1], z: data.scale[2] };
  }
  if (data.rotation && Array.isArray(data.rotation)) {
    data.rotation = { x: data.rotation[0], y: data.rotation[1], z: data.rotation[2] };
  }
  if (data.direction && Array.isArray(data.direction)) {
    data.direction = { x: data.direction[0], y: data.direction[1], z: data.direction[2] };
  }
  return data;
}
