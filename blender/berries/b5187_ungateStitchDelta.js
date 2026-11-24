// ungateStitchDelta
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/tuner/scripts/patch-maplibre-terrain-clip.mjs, line 190
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ELE_DELTA_STITCH = 'float ele_delta=a_pos3d.z==1.0 ? u_ele_delta : 0.0;';

const ELE_DELTA_GATED =
  'float ele_delta=(a_pos3d.z==1.0 && u_clip_enabled<0.5) ? u_ele_delta : 0.0;';


function ungateStitchDelta(s) {
  if (s.includes(ELE_DELTA_STITCH)) {
    s = s.split(ELE_DELTA_STITCH).join(ELE_DELTA_GATED);
  }
  return s;
}
