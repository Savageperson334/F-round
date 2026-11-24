// cdn
//
// Copied verbatim from https://github.com/forkwiki/fork
//   file netlify/functions/market.mjs, line 35
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Archaeology, caves, museums, archival fragments
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const cdn = s => ({ 'cache-control': `public, max-age=${Math.min(s, 15)}`, 'netlify-cdn-cache-control': `public, s-maxage=${s}, stale-while-revalidate=${s * 3}`, 'netlify-vary': 'query' });
