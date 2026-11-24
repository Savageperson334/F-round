// cssLength
//
// Copied verbatim from https://github.com/hazymorning/origami_weather
//   file src/origami-weather.js, line 1513
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const _CSS_STRIP = /["'<>;{}\\]|\/\*|\*\/|@|url\s*\(|expression\s*\(/gi;


const cssValue = (v) => String(v).replace(/[\u0000-\u001F\u007F]/g, '').replace(_CSS_STRIP, '');


function normalizeLength(v) {
    const s = String(v == null ? '' : v).trim();
    if (!s) return '';
    return s.split(/\s+/).map(tok => {
        if (!tok) return tok;
        if (tok === '0') return '0px';
        return /^[+-]?(\d+\.?\d*|\.\d+)$/.test(tok) ? tok + 'px' : tok;
    }).join(' ');
}


function cssLength(v) { return cssValue(normalizeLength(v)); }
