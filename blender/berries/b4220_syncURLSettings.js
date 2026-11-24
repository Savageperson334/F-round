// syncURLSettings
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file demo/settings.js, line 84
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function syncURLSettings(settings, url) {
    for (var property in settings) {
        if (!settings.hasOwnProperty(property) || typeof settings[property] === 'function') continue;
        url.searchParams.set(property, String(settings[property]));
    }
    return url;
}
