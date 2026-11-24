// sorted_record
//
// Copied verbatim from https://github.com/XiaoJiang-Phy/CrystalCanvas
//   file scripts/ipc-inventory.mjs, line 55
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function sorted_record(record) {
    return Object.fromEntries(Object.entries(record)
        .sort(([left], [right]) => left.localeCompare(right))
        .map(([key, values]) => [key, Array.isArray(values) ? [...values].sort() : values]));
}
