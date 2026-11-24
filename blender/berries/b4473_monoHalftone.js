// monoHalftone
//
// Copied verbatim from https://github.com/NaitLee/Cat-Printer
//   file www/image.js, line 58
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Thermal printers and obsolete output
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function monoHalftone(mono, w, h) {
    const spot = 4;
    const spot_h = 4 / 2 + 1;
    const spot_s = 4 * 4;
    let i, j, x, y, o = 0.0;
    for(j = 0; j < h - 4; j += spot){
        for(i = 0; i < w - 4; i += spot){
            for(x = 0; x < 4; ++x)for(y = 0; y < 4; ++y)o += mono[(j + y) * w + i + x];
            o = (1 - o / spot_s / 0xff) * spot;
            for(x = 0; x < 4; ++x)for(y = 0; y < 4; ++y){
                mono[(j + y) * w + i + x] = Math.abs(x - spot_h) >= o || Math.abs(y - spot_h) >= o ? 0xff : 0x00;
            }
        }
        for(; i < w; ++i)mono[j * w + i] = 0xff;
    }
    for(; j < h; ++j)for(i = 0; i < w; ++i)mono[j * w + i] = 0xff;
    return mono;
}
