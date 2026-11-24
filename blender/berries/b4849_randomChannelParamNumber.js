// randomChannelParamNumber
//
// Copied verbatim from https://github.com/asyncapi-archived-repos/simulator
//   file src/RequestHandler/mqttHandler.js, line 3
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function randomChannelParamNumber (min,max) {
  return Math.floor(Math.random() * max); //NOSONAR
}
