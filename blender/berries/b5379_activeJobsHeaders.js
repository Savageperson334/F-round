// activeJobsHeaders
//
// Copied verbatim from https://github.com/microsoft/haste
//   file ui/src/Components/Home/activeJobsRequest.js, line 12
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function activeJobsHeaders(etag) {
  const headers = {};
  if (etag) headers["If-None-Match"] = etag;
  return headers;
}
