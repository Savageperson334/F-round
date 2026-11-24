// split
//
// Copied verbatim from https://github.com/adamgilman/Orrery
//   file tools/packs/build.mjs, line 94
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const GLUED = /(Identity|Cost|Tools)(and)(?=[A-Z])|(Distro|Lookout|Lightsail|Sx|Streaming|Service|Workflows)(for)(?=[A-Z])|(Database)(at)(?=[A-Z])|(Site)(to)(?=[A-Z])|(S3|Net|Torch|Flow|Service)(on)(?=[A-Z])/g;


const split = (s) => s.replace(GLUED, (m, ...g) => { const [a, w] = g.filter((x) => typeof x === "string"); return `${a} ${w}`; }).replace(/([a-z\d])([A-Z])/g, "$1 $2").replace(/([A-Z]+)([A-Z][a-z])/g, "$1 $2").replace(/([a-z])(\d)/g, "$1 $2").replace(/_/g, " ");
