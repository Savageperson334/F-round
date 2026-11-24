// HostOrder
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 245
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const PT = {
  FIRE_ON: 0, FIRE: 1, AUDIO: 2, BAND: 3, GAIN: 4, BIAS: 5, COIL_LAG: 6, THRESHOLD: 7, PULSE: 8,
  MAGNET: 9, COIL_SIZE: 10, COIL_SPREAD: 11,
  FLUID: 12, VISCOSITY: 13, NOISE: 14, SETTLE: 15,
  FIELD_WIDTH: 16, TILT: 17, HEIGHT: 18, EXPOSURE: 19, LIGHTS: 20, BACKDROP: 21, MIX: 22,
  ABOUT_TEXT: 23,
};


function HostOrder(effect) {
  const order = [];
  for (let id = 0; id < PT.ABOUT_TEXT; id += 1) {
    const overOnly = id === PT.HEIGHT || id === PT.MIX;
    const sourceOnly = id === PT.LIGHTS || id === PT.BACKDROP;
    if ((effect && sourceOnly) || (!effect && overOnly)) continue;
    order.push(id);
  }
  return order;
}
