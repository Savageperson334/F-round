// describeSysex
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/app.js, line 284
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SYSEX_MFR = {
  "01": "Sequential", "04": "Moog", "06": "Lexicon", "07": "Kurzweil", "0F": "Ensoniq", "10": "Oberheim",
  "11": "Apple", "18": "E-mu", "1C": "Eventide", "40": "Kawai", "41": "Roland", "42": "Korg", "43": "Yamaha",
  "44": "Casio", "47": "Akai", "52": "Zoom", "7D": "Non-commercial", "7E": "Universal Non-Real Time",
  "7F": "Universal Real Time",
  "00 00 0E": "Alesis", "00 20 1F": "TC Electronic", "00 20 29": "Focusrite/Novation", "00 20 32": "Behringer",
  "00 20 33": "Access", "00 20 3C": "Elektron", "00 20 6B": "Arturia", "00 21 09": "Native Instruments",
};


const hex = (bytes) => [...bytes].map((b) => b.toString(16).padStart(2, "0").toUpperCase()).join(" ");


function sysexMfr(d, i = 1) {
  const id = d[i] === 0 ? hex(d.slice(i, i + 3)) : hex([d[i] ?? 0]);
  return { id, name: SYSEX_MFR[id] || "unknown maker", len: d[i] === 0 ? 3 : 1 };
}


function describeSysex(d) {
  const end = d[d.length - 1] === 0xf7 ? d.length - 1 : d.length;
  const sub = (a, b) => d[3] === a && d[4] === b;
  if (d[1] === 0x7e) {
    if (sub(0x06, 0x01)) return `SysEx Identity request (device ${d[2] === 0x7f ? "all" : d[2]})`;
    if (sub(0x06, 0x02) && end > 5) {
      const who = sysexMfr(d, 5), o = 5 + who.len;
      if (o + 8 <= end)
        return `SysEx Identity reply: ${who.name} (${who.id}), family ${hex(d.slice(o, o + 2))}, model ${hex(d.slice(o + 2, o + 4))}, version ${hex(d.slice(o + 4, o + 8))}`;
      return `SysEx Identity reply: ${who.name} (${who.id})`;
    }
    if (sub(0x09, 0x01)) return "SysEx GM System On";
    if (sub(0x09, 0x02)) return "SysEx GM System Off";
    return `SysEx Universal Non-RT ${hex([d[3] ?? 0, d[4] ?? 0])} (${d.length} bytes)`;
  }
  if (d[1] === 0x7f) {
    if (sub(0x04, 0x01)) return `SysEx Master Volume ${d[6] ?? 0}`;
    return `SysEx Universal RT ${hex([d[3] ?? 0, d[4] ?? 0])} (${d.length} bytes)`;
  }
  if (d[1] === 0x43 && d.length === 7 && (d[2] & 0xf0) === 0x10 && d[3] < 2)
    return `SysEx Yamaha (43) parameter change ${d[3] * 128 + d[4]} = ${d[5]}`; // DX7-style VCED
  const m = sysexMfr(d);
  return `SysEx ${m.name} (${m.id}), ${d.length} bytes`;
}
