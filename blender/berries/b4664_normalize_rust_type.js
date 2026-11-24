// normalize_rust_type
//
// Copied verbatim from https://github.com/XiaoJiang-Phy/CrystalCanvas
//   file scripts/ipc-inventory.mjs, line 222
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Molecular shapes and crystal lattices
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function normalize_rust_type(type) {
    return type.replace(/\s+/g, ' ').trim();
}
