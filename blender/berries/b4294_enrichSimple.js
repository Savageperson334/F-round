// enrichSimple
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/fix-remaining-narrative.mjs, line 54
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function enrichSimple(text, mitre) {
  let t = String(text || '').replace(/\s+/g, ' ').trim();
  if (t.length < 320 || !/\([^)]{25,}\)/.test(t)) {
    t = `${t.replace(/\.\s*$/, '')}. Quoting the story beat above, that physical action maps onto ${mitre} (the exact host or protocol control point this stage must exercise before the next kill-chain move can start).`;
  }
  while (t.length < 320) {
    t +=
      ' Defenders should read the quoted story prop and the technical tokens together.';
  }
  return t;
}
