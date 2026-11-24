// init_array
//
// Copied verbatim from https://github.com/toruseo/traffic-flow-demo
//   file util.js, line 9
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function init_array(length, init){
    var arr = Array(length)
    arr.fill(init)
    return arr
}
