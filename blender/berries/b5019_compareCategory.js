// compareCategory
//
// Copied verbatim from https://github.com/fenderberg/fm1-sy1
//   file app/site/manager/library.js, line 6
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const CATEGORY_ORDER = [0,1,2,3,4,5,8,9,10,11,12,6,7];


const compareCategory = (a,b) => CATEGORY_ORDER.indexOf(a) - CATEGORY_ORDER.indexOf(b);
