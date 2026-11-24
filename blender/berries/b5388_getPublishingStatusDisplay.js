// getPublishingStatusDisplay
//
// Copied verbatim from https://github.com/microsoft/haste
//   file ui/src/util/publishing.js, line 23
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const STATUS_DISPLAY = {
  PENDING: { label: "Queued", color: "warning" },
  IN_PROGRESS: { label: "Publishing", color: "warning" },
  PUBLISHED: { label: "Published", color: "success" },
  FAILED: { label: "Failed", color: "danger" },
  UNPUBLISH_PENDING: { label: "Cleanup queued", color: "warning" },
  UNPUBLISHING: { label: "Unpublishing", color: "warning" },
  UNPUBLISH_FAILED: { label: "Cleanup failed", color: "danger" },
};


function getPublishingStatusDisplay(status) {
  return STATUS_DISPLAY[status] || { label: status, color: "informative" };
}
