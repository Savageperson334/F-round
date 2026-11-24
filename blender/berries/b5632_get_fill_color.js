// get_fill_color
//
// Copied verbatim from https://github.com/pyrocko/pyrocko
//   file src/gui/snuffler/snufflings/map/map_util.js, line 85
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Earthquakes and seismic tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function get_fill_color(depth, depth_min, depth_max){
    if (depth_min==depth_max)
        scale = 0.5;
    else
        var scale = (depth-depth_min)/(depth_max-depth_min);
    var r = parseInt(255 * scale);
    var b = parseInt(255 * (1-scale));
    return 'rgba(' + r + ',0,'+ b + ',0.5)';
}
