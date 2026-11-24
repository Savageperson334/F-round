// enrichStory
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/fix-narrative-mod-fields.mjs, line 31
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function strip(s) {
  return String(s || '')
    .replace(/—/g, '-')
    .replace(/\s+/g, ' ')
    .trim();
}


function enrichStory(text, stepNumber) {
  let t = strip(text);
  if (t.length >= 180) return t;
  const add =
    stepNumber <= 1
      ? ' The operator keeps using the same physical props and room layout from the briefing story so every later movement stays visually continuous for the 3D beat.'
      : ' Continuing the same characters and room from the previous beat, the operator performs two more concrete physical movements that an animator can stage without guessing.';
  t = `${t.replace(/\.\s*$/, '')}.${add}`;
  if (t.length < 180) {
    t +=
      ' Each newly introduced prop is used for one explicit job before the next stage begins.';
  }
  return strip(t);
}
