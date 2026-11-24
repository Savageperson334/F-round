// vector3ToArray
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/operation/mesh.js, line 175
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function vector3ToArray(data) {
  // change all objects (position, scale, rotation) inside the data form {x: 0, y: 0, z: 0} to [0, 0, 0]
  // if position exists and is an object, convert it to array
  const newdata = { ...data };
  if (data.position && !Array.isArray(data.position)) {
    newdata.position = [data.position.x, data.position.y, data.position.z];
  }
  if (data.scale && !Array.isArray(data.scale)) {
    newdata.scale = [data.scale.x, data.scale.y, data.scale.z];
  }
  if (data.rotation && !Array.isArray(data.rotation)) {
    newdata.rotation = [data.rotation.x, data.rotation.y, data.rotation.z];
  }
  if (data.direction && !Array.isArray(data.direction)) {
    newdata.direction = [data.direction.x, data.direction.y, data.direction.z];
  }
  return newdata;
}
