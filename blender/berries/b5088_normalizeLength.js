// normalizeLength
//
// Copied verbatim from https://github.com/hazymorning/origami_weather
//   file src/origami-weather.js, line 1504
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function normalizeLength(v) {
    const s = String(v == null ? '' : v).trim();
    if (!s) return '';
    return s.split(/\s+/).map(tok => {
        if (!tok) return tok;
        if (tok === '0') return '0px';
        return /^[+-]?(\d+\.?\d*|\.\d+)$/.test(tok) ? tok + 'px' : tok;
    }).join(' ');
}
