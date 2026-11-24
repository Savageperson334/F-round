// clipMeshToPlanes
//
// Copied verbatim from https://github.com/superstar54/weas
//   file src/geometry/marchingCubes.js, line 375
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function clipTrianglesAgainstPlane(positions, faces, normal, point, eps) {
  if (!Array.isArray(faces) || faces.length === 0) {
    return { positions, faces };
  }

  const vList = positions.map((p) => [p[0], p[1], p[2]]);
  const outFaces = [];

  const n0 = normal[0];
  const n1 = normal[1];
  const n2 = normal[2];
  const p0 = point[0];
  const p1 = point[1];
  const p2 = point[2];

  const signedDistance = (p) => n0 * (p[0] - p0) + n1 * (p[1] - p1) + n2 * (p[2] - p2);

  for (let i = 0; i < faces.length; i += 3) {
    const ia = faces[i];
    const ib = faces[i + 1];
    const ic = faces[i + 2];
    const tri = [vList[ia], vList[ib], vList[ic]];
    const da = signedDistance(tri[0]);
    const db = signedDistance(tri[1]);
    const dc = signedDistance(tri[2]);
    const inside = [da <= eps, db <= eps, dc <= eps];

    if (inside[0] && inside[1] && inside[2]) {
      outFaces.push(ia, ib, ic);
      continue;
    }
    if (!inside[0] && !inside[1] && !inside[2]) {
      continue;
    }

    const poly = tri;
    const polyD = [da, db, dc];
    const newPoly = [];
    for (let j = 0; j < 3; j++) {
      const a = poly[j];
      const daj = polyD[j];
      const b = poly[(j + 1) % 3];
      const dbj = polyD[(j + 1) % 3];
      const aIn = daj <= eps;
      const bIn = dbj <= eps;
      if (aIn) {
        newPoly.push(a);
      }
      if (aIn !== bIn) {
        const t = daj / (daj - dbj);
        newPoly.push([a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]), a[2] + t * (b[2] - a[2])]);
      }
    }

    if (newPoly.length < 3) continue;
    const base = vList.length;
    for (let j = 0; j < newPoly.length; j++) {
      vList.push(newPoly[j]);
    }
    for (let j = 1; j < newPoly.length - 1; j++) {
      outFaces.push(base, base + j, base + j + 1);
    }
  }

  return { positions: vList, faces: outFaces };
}


function clipMeshToPlanes(positions, faces, planes, eps = 1e-10) {
  if (!Array.isArray(planes) || planes.length === 0) {
    return { positions, faces };
  }

  let vOut = positions;
  let fOut = faces;
  for (let i = 0; i < planes.length; i++) {
    const plane = planes[i];
    if (!plane || !plane.normal || !plane.point) continue;
    const clipped = clipTrianglesAgainstPlane(vOut, fOut, plane.normal, plane.point, eps);
    vOut = clipped.positions;
    fOut = clipped.faces;
    if (!fOut.length) break;
  }

  return { positions: vOut, faces: fOut };
}
