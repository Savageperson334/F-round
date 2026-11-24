// forecastFingerprint
//
// Copied verbatim from https://github.com/hazymorning/origami_weather
//   file src/origami-weather.js, line 1608
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function forecastFingerprint(forecast) {
    if (!forecast || !forecast.length) return '';
    let s = '' + forecast.length;
    for (const f of forecast) s += `|${f.datetime}|${f.condition}|${f.temperature}|${f.templow != null ? f.templow : ''}|${f.precipitation_probability != null ? f.precipitation_probability : ''}`;
    return s;
}
