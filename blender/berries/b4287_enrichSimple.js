// enrichSimple
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/fix-narrative-mod-fields.mjs, line 46
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


function enrichSimple(text, stage, mitre) {
  let t = strip(text);
  const specs = (stage?.keySpecs || []).slice(0, 2);
  const specText = specs.length ? specs.join(' and ') : mitre;
  if (t.length < 320 || !/\([^)]{25,}\)/.test(t)) {
    const add = ` Quoting the story beat above, that physical action maps onto ${specText} (the exact host or protocol control point this stage must exercise before the next kill-chain move can start).`;
    t = `${t.replace(/\.\s*$/, '')}.${add}`;
  }
  while (t.length < 320) {
    t +=
      ' Defenders should read the quoted story prop and the technical tokens together so the bridge stays unambiguous.';
  }
  return strip(t);
}
