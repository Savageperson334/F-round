// estimateDroppedFrames
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/runtime/benchmark-vector-tuning.mjs, line 424
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const IDEAL_FRAME_MS = 1000 / 60;


function estimateDroppedFrames(samples, idealFrameMs) {
  const budget = Number.isFinite(idealFrameMs) && idealFrameMs > 0
    ? idealFrameMs
    : IDEAL_FRAME_MS;
  return samples.filter(Number.isFinite).reduce(function (sum, duration) {
    return sum + Math.max(0, Math.round(duration / budget) - 1);
  }, 0);
}
