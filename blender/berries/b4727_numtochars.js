// numtochars
//
// Copied verbatim from https://github.com/ahmedibrahimq/braille-it
//   file braille.js, line 52
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Braille and tactile information
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

var map_09_aj = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}


function numtochars(num) {
    var nums = num.split("");
    for (let i = 0; i < nums.length; i++) {
        const n = nums[i];
        nums[i] = map_09_aj[n];
    }
    return nums.join("");
}
