// scaleData
//
// Copied verbatim from https://github.com/adamgilman/Orrery
//   file tools/packs/build.mjs, line 228
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const ARITY = { m: 2, l: 2, t: 2, h: 1, v: 1, c: 6, s: 4, q: 4, a: 7, z: 0 };


const round = (n) => String(Math.round(n * 1000) / 1000);


function scaleData(d, k) {
  return d.replace(/([a-zA-Z])([^a-zA-Z]*)/g, (_, cmd, rest) => {
    if (!ARITY[cmd.toLowerCase()]) return cmd;
    const nums = (rest.match(/-?\d*\.?\d+/g) ?? []).map(Number);
    return cmd + nums.map((v, i) => round(cmd.toLowerCase() === "a" && [2, 3, 4].includes(i % 7) ? v : v * k)).join(" ");
  });
}
