// enrichStory
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/fix-remaining-narrative.mjs, line 43
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function enrichStory(text) {
  let t = String(text || '').replace(/\s+/g, ' ').trim();
  if (t.length < 180) {
    t = `${t.replace(/\.\s*$/, '')}. Continuing the same characters and room from the previous beat, the operator performs two more concrete physical movements that an animator can stage without guessing, and each newly introduced prop has one explicit job.`;
  }
  while (t.length < 180) {
    t += ' The props stay inside the same building as the briefing story.';
  }
  return t;
}
