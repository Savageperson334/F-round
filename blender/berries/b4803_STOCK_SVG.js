// STOCK_SVG
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/fwcards.js, line 208
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const STOCK_SVG = (s) => '<svg viewBox="0 0 24 24" aria-hidden="true"><circle class="bg" cx="12" cy="12" r="10.5"/>'
  + `<circle class="ring" cx="12" cy="12" r="8.6"/><text class="fg-text" x="12" y="14.9" text-anchor="middle">${s.replace(/[^A-Za-z0-9.]/g, "")}</text></svg>`;
