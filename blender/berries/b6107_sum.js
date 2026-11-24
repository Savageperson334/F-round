// sum
//
// Copied verbatim from https://github.com/toruseo/traffic-flow-demo
//   file util.js, line 3
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function sum(arr){
    return arr.reduce(function(sum, element){
        return sum + element
    }, 0)
}
