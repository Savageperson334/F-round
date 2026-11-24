// apply_serde_case
//
// Copied verbatim from https://github.com/XiaoJiang-Phy/CrystalCanvas
//   file scripts/ipc-inventory.mjs, line 412
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function pascal_to_snake(name) {
    return name
        .replace(/([A-Z]+)([A-Z][a-z])/g, '$1_$2')
        .replace(/([a-z0-9])([A-Z])/g, '$1_$2')
        .toLowerCase();
}


function words(name) {
    return pascal_to_snake(name).split('_');
}


function apply_serde_case(name, style) {
    if (!style) return name;
    const parts = words(name);
    if (style === 'lowercase') return parts.join('');
    if (style === 'UPPERCASE') return parts.join('').toUpperCase();
    if (style === 'snake_case') return parts.join('_');
    if (style === 'SCREAMING_SNAKE_CASE') return parts.join('_').toUpperCase();
    if (style === 'kebab-case') return parts.join('-');
    if (style === 'SCREAMING-KEBAB-CASE') return parts.join('-').toUpperCase();
    if (style === 'camelCase') return parts[0] + parts.slice(1).map((part) => part[0].toUpperCase() + part.slice(1)).join('');
    if (style === 'PascalCase') return parts.map((part) => part[0].toUpperCase() + part.slice(1)).join('');
    return name;
}
