// strip_rust_attributes
//
// Copied verbatim from https://github.com/XiaoJiang-Phy/CrystalCanvas
//   file scripts/ipc-inventory.mjs, line 208
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function matching_delimiter(source, opening_index, opening, closing) {
    let depth = 0;
    for (let index = opening_index; index < source.length; index += 1) {
        if (source[index] === opening) depth += 1;
        if (source[index] === closing) depth -= 1;
        if (depth === 0) return index;
    }
    return -1;
}


function strip_rust_attributes(parameter) {
    let result = parameter.trim();
    while (result.startsWith('#[')) {
        const closing = matching_delimiter(result, 1, '[', ']');
        if (closing < 0) break;
        result = result.slice(closing + 1).trim();
    }
    return result;
}
