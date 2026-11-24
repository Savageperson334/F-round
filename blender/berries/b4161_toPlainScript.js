// toPlainScript
//
// Copied verbatim from https://github.com/Chienlin1014/Orrery
//   file build.mjs, line 60
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const IMPORT_RE = /^\s*import\s+(?:[\s\S]*?)\s+from\s*['"](\.[^'"]+)['"];?\s*$/gm;

const BARE_IMPORT_RE = /^\s*import\s*['"](\.[^'"]+)['"];?\s*$/gm;


function toPlainScript(source) {
  return source
    .replace(IMPORT_RE, '')
    .replace(BARE_IMPORT_RE, '')
    // `export { a, b };` re-export lists carry no declaration.
    .replace(/^\s*export\s*\{[^}]*\}\s*;?\s*$/gm, '')
    // `export function f` / `export const x` / `export class C`
    .replace(/^(\s*)export\s+(function|const|let|var|class|async)\b/gm, '$1$2');
}
