// splitCss
//
// Copied verbatim from https://github.com/hazymorning/origami_weather
//   file src/origami-weather.js, line 1514
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function splitCss(v) {
    const out = [];
    let depth = 0, cur = '';
    for (const ch of v) {
        depth += ch === '(' ? 1 : ch === ')' ? -1 : 0;
        if (!depth && /\s/.test(ch)) { if (cur) out.push(cur); cur = ''; } else cur += ch;
    }
    return cur ? [...out, cur] : out;
}
