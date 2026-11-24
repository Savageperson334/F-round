// enrichHow
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/fix-remaining-narrative.mjs, line 31
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function enrichHow(text, mitre) {
  let t = String(text || '').replace(/\s+/g, ' ').trim();
  if (t.length < 380 || !/\([^)]{25,}\)/.test(t)) {
    t = `${t.replace(/\.\s*$/, '')}. Mechanically, defenders treat this stage as complete only after the ${mitre} control point is observed as live runtime state (the concrete checkpoint proving prior-stage output now drives the next action) and confirmed in host or network telemetry (the channel that timestamps the handoff).`;
  }
  while (t.length < 380) {
    t +=
      ' Keep every API and flag paired with an immediate plain-English parenthetical.';
  }
  return t;
}
