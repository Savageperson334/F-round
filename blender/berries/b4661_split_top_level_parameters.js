// split_top_level_parameters
//
// Copied verbatim from https://github.com/XiaoJiang-Phy/CrystalCanvas
//   file scripts/ipc-inventory.mjs, line 180
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function split_top_level_parameters(source) {
    const parameters = [];
    let start = 0;
    let angle_depth = 0;
    let parenthesis_depth = 0;
    let bracket_depth = 0;
    let brace_depth = 0;
    for (let index = 0; index < source.length; index += 1) {
        const character = source[index];
        if (character === '<') angle_depth += 1;
        else if (character === '>') angle_depth -= 1;
        else if (character === '(') parenthesis_depth += 1;
        else if (character === ')') parenthesis_depth -= 1;
        else if (character === '[') bracket_depth += 1;
        else if (character === ']') bracket_depth -= 1;
        else if (character === '{') brace_depth += 1;
        else if (character === '}') brace_depth -= 1;
        else if (character === ',' && angle_depth === 0 && parenthesis_depth === 0
            && bracket_depth === 0 && brace_depth === 0) {
            parameters.push(source.slice(start, index).trim());
            start = index + 1;
        }
    }
    const tail = source.slice(start).trim();
    if (tail) parameters.push(tail);
    return parameters;
}
