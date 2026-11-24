// normalize
//
// Copied verbatim from https://github.com/ahmedibrahimq/braille-it
//   file braille.js, line 27
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


function normalize(texten) {
    var vocabs = texten.split(" ");
    for (let i = 0; i < vocabs.length; i++) {
        const vocab = vocabs[i];
        if (/\b\d+\b/.test(vocab)) { // If the word contains numbers only
            vocabs[i] = '#' + numtochars(vocab); // put a flag to know that
        } else {
            vocabs[i] = normalizeChars(vocab);
        }
        
    }
    return vocabs.join(" ");
}
