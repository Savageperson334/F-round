// mm
//
// Copied verbatim from https://github.com/experimentalDataAesthetics/play-splom
//   file app/selectors/sound.js, line 31
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const mm = (prev, num) => {
  const p = prev || { min: Number.MAX_VALUE, max: Number.MIN_VALUE };
  return {
    min: Math.min(p.min, num),
    max: Math.max(p.max, num)
  };
};
