// theme_css
//
// Copied verbatim from https://github.com/aritraroy24/obsidian-matterviz
//   file main.js, line 67
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function theme_css(is_dark) {
  return is_dark ? `
      --mv-bg: #1e1e1e;
      --mv-fg: #d4d4d4;
      --mv-border: rgba(255,255,255,0.12);
      --mv-accent: #007fd4;
      --mv-error: #f85149;` : `
      --mv-bg: #ffffff;
      --mv-fg: #333333;
      --mv-border: rgba(0,0,0,0.12);
      --mv-accent: #0078d4;
      --mv-error: #d32f2f;`;
}
