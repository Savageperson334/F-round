// iconSvg
//
// Copied verbatim from https://github.com/YaseenHQ/Shipwreck
//   file media/brand/render.js, line 12
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Shipwrecks and maritime ghosts
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function iconSvg(glyph) {
  const inner = glyph.replace(/^[\s\S]*?<svg[^>]*>/, "").replace(/<\/svg>\s*$/, "");
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#151a24"/>
      <stop offset="1" stop-color="#0b0d12"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="112" fill="url(#bg)"/>
  <svg x="76" y="70" width="360" height="360" viewBox="0 0 64 64" fill="#f4f6fb" color="#f4f6fb">${inner}</svg>
</svg>
`;
}
