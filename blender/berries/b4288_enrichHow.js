// enrichHow
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/fix-narrative-mod-fields.mjs, line 61
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


function enrichHow(text, stage, mitre) {
  let t = strip(text);
  const log = stage?.logs?.[0];
  const specs = (stage?.keySpecs || []).slice(0, 2);
  const specText = specs.length ? specs.join(' and ') : mitre;
  if (t.length < 380 || !/\([^)]{25,}\)/.test(t)) {
    let add = ` Mechanically, this stage is complete only after ${specText} is observed as live runtime state (the concrete checkpoint proving the previous stage's output now drives the next action).`;
    if (log?.source) {
      add += ` Operators usually confirm that transition in ${strip(String(log.source))}${
        log.EventCode != null ? ` Event ${log.EventCode}` : ''
      } (the telemetry channel that timestamps this handoff for later reconstruction).`;
    }
    t = `${t.replace(/\.\s*$/, '')}.${add}`;
  }
  while (t.length < 380) {
    t +=
      ' Keep every API, flag, and handle paired with an immediate plain-English parenthetical so the deep-dive never becomes a jargon dump.';
  }
  return strip(t);
}
