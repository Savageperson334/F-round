// normalizeChars
//
// Copied verbatim from https://github.com/ahmedibrahimq/braille-it
//   file braille.js, line 41
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Braille and tactile information
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

var map_09_aj = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '0': 'j'}


function normalizeChars(word){
    var tokens = word.split("");
    for (let j = 0; j < tokens.length; j++) {
        const c = tokens[j];
        if (/[A-Z]/.test(c)) {tokens[j] = '^' + c.toLowerCase();} //Capital letter, put capital affix
        else if (/\d/.test(c)) {tokens[j] = '#' + map_09_aj[c];} // number, put number sign affix & map nums to letters
        else if (/\*/.test(c)) {tokens[j] = c + c;} // asterisk* duplicate its symbol
    }
    return tokens.join("");
    }
