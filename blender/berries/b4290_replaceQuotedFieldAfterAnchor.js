// replaceQuotedFieldAfterAnchor
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/fix-narrative-mod-fields.mjs, line 106
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function esc(s) {
  return String(s)
    .replace(/\\/g, '\\\\')
    .replace(/'/g, "\\'")
    .replace(/\n/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}


function replaceQuotedFieldAfterAnchor(src, anchorRegex, fieldName, newValue) {
  const m = src.match(anchorRegex);
  if (!m) return { ok: false, reason: 'anchor not found', src };
  const from = m.index + m[0].length;
  const fieldIdx = src.indexOf(`${fieldName}:`, from);
  if (fieldIdx < 0 || fieldIdx - from > 2500) {
    return { ok: false, reason: `${fieldName} not near anchor`, src };
  }
  let i = fieldIdx + fieldName.length + 1;
  while (i < src.length && /\s/.test(src[i])) i++;
  const quote = src[i];
  if (quote !== "'" && quote !== '"' && quote !== '`') {
    return { ok: false, reason: `${fieldName} not string`, src };
  }
  let j = i + 1;
  while (j < src.length) {
    if (src[j] === '\\') {
      j += 2;
      continue;
    }
    if (src[j] === quote) break;
    j++;
  }
  if (j >= src.length) return { ok: false, reason: 'unclosed string', src };
  // If premature close due to raw apostrophe, fall forward to next field key
  let end = j;
  const after = src[j + 1] || '';
  if (quote === "'" && /[A-Za-z]/.test(after)) {
    const next = src.slice(i).search(
      /\n\s*(storyAnalogy|simpleExplanation|howItWorksInPractice|detectionAndEvidence|diagramAlignment|plainTitle|mitreId|stepNumber)\s*:/
    );
    if (next < 0) return { ok: false, reason: 'cannot rescan field end', src };
    // rebuild line-ish
    const lineStart = src.lastIndexOf('\n', fieldIdx) + 1;
    const indent = src.slice(lineStart).match(/^(\s*)/)[1];
    const absNext = i + next;
    const nextLine = src.lastIndexOf('\n', absNext) + 1;
    const rebuilt =
      src.slice(0, lineStart) +
      `${indent}${fieldName}:\n${indent}  '${esc(newValue)}',` +
      src.slice(nextLine > lineStart ? nextLine : absNext);
    return { ok: true, src: rebuilt };
  }
  const next = src.slice(0, i + 1) + esc(newValue) + src.slice(end);
  return { ok: true, src: next };
}
