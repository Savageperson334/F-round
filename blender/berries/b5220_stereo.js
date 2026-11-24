// stereo
//
// Copied verbatim from https://github.com/jb3/meeple
//   file web/audio/core.js, line 163
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Peculiar interfaces, worlds, visual systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function stereo(node) {
  node.channelCount = 2;
  node.channelCountMode = "explicit";
  node.channelInterpretation = "speakers";
  return node;
}
