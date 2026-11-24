// cleanAnalytic
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file demo/analytics.js, line 62
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function roundNumber(value, places) {
    places = places || 0;
    var multiplier = Math.pow(10, places | 0);
    return Math.round(value * multiplier) / multiplier;
}


function cleanAnalytic(value) {
    if (Array.isArray(value)) {
        if (value.length === 1) value = value[0];
        else {
            var text = value.map(function(item) { return Math.round(item); }).join(', ');
            if (text.length > 9) text = value.join(',');
            if (text.length > 9) text = text.substring(0, text.lastIndexOf(',', 7)) + ',…';
            return text;
        }
    }
    var integerText = (value | 0) + '',
        padding = '';
    if ((value | 0) === 0 && value < 0) integerText = '-' + integerText;
    while (integerText.length + padding.length < 5) padding += ' ';
    return padding + roundNumber(typeof value === 'undefined' || value === null ? NaN : value, 3);
}
