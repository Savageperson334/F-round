// pickExportFrames
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/runtime/qa.mjs, line 61
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function runs(flags) {
  const out = [];
  let from = -1;
  for (let i = 0; i <= flags.length; i++) {
    if (i < flags.length && flags[i]) { if (from < 0) from = i; }
    else if (from >= 0) { out.push([from, i - 1]); from = -1; }
  }
  return out;
}


function pickExportFrames(story, fps, total, hasMapLayer) {
  const cards = story.cards || [];
  const visible = (i) => cards.filter((c) => i / fps >= c.t0 && i / fps < c.t1).length;
  const clamp = (i) => Math.max(0, Math.min(total - 1, i));
  const counts = Array.from({ length: total }, (_, i) => visible(i));

  const first = cards.slice().sort((a, b) => a.t0 - b.t0)[0];
  const caption = first ? clamp(Math.round(((first.t0 + first.t1) / 2) * fps)) : 0;

  const max = Math.max(...counts);
  const peakRuns = runs(counts.map((c) => c === max));
  const pr = peakRuns[0] || [0, 0];
  const peak = Math.floor((pr[0] + pr[1]) / 2);

  const min = Math.min(...counts);
  const nocaption = hasMapLayer ? caption : counts.indexOf(min);

  const moving = (story.shots || []).find((s, k) => k > 0 && s.move > 0);
  const handoff = moving ? clamp(Math.round((moving.t - moving.move / 2) * fps)) : clamp(Math.floor(total / 2));
  return { caption, nocaption, peak, handoff, peakCards: max };
}
