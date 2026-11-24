// statistics
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/runtime/benchmark-vector-tuning.mjs, line 433
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function rounded(value, digits) {
  if (!Number.isFinite(value)) return null;
  return Number(value.toFixed(digits == null ? 2 : digits));
}


function percentile(values, ratio) {
  const selected = values.filter(Number.isFinite).slice().sort(function (a, b) {
    return a - b;
  });
  if (!selected.length) return null;
  return selected[Math.min(selected.length - 1, Math.ceil(selected.length * ratio) - 1)];
}


function statistics(values, digits) {
  const selected = values.filter(Number.isFinite);
  if (!selected.length) {
    return {
      count: 0,
      min: null,
      max: null,
      mean: null,
      p50: null,
      p95: null,
      p99: null,
    };
  }
  const sum = selected.reduce(function (total, value) {
    return total + value;
  }, 0);
  return {
    count: selected.length,
    min: rounded(Math.min.apply(Math, selected), digits),
    max: rounded(Math.max.apply(Math, selected), digits),
    mean: rounded(sum / selected.length, digits),
    p50: rounded(percentile(selected, 0.5), digits),
    p95: rounded(percentile(selected, 0.95), digits),
    p99: rounded(percentile(selected, 0.99), digits),
  };
}
