// trophySVG
//
// Copied verbatim from https://github.com/pshenok/server-survival
//   file src/achievements/ui.js, line 26
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function trophySVG(extraClass) {
    return `<svg class="w-8 h-8 ${extraClass}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M8 21h8" />
        <path d="M12 17v4" />
        <path d="M7 4h10v5a5 5 0 0 1-10 0z" />
        <path d="M7 6H4a1 1 0 0 0-1 1 4 4 0 0 0 4 4" />
        <path d="M17 6h3a1 1 0 0 1 1 1 4 4 0 0 1-4 4" />
    </svg>`;
}
