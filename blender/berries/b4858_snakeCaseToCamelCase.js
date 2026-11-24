// snakeCaseToCamelCase
//
// Copied verbatim from https://github.com/cds-astro/ipyaladin
//   file js/utils.js, line 6
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function snakeCaseToCamelCase(snakeCaseStr) {
  if (snakeCaseStr.charAt(0) === "_") snakeCaseStr = snakeCaseStr.slice(1);
  let temp = snakeCaseStr.split("_");
  for (let i = 1; i < temp.length; i++)
    temp[i] = temp[i].charAt(0).toUpperCase() + temp[i].slice(1);
  return temp.join("");
}
