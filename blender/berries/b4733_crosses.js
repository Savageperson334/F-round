// crosses
//
// Copied verbatim from https://github.com/alexbarakov/amsterdam-by-building
//   file web/app.js, line 938
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const crosses = (n, of = 3) => `<span class="q-x" aria-hidden="true">${Array.from({ length: of }, (_, i) =>
  `<i class="${i < n ? 'on' : ''}">×</i>`).join('')}</span>`;
