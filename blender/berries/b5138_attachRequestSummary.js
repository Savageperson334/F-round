// attachRequestSummary
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/runtime/verify-vector-layers.mjs, line 634
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const requestRecords = [];


function increment(obj, key) {
  key = String(key || 'unknown');
  obj[key] = (obj[key] || 0) + 1;
}


function summarizeRequests(startEpochMs, endEpochMs) {
  const selected = requestRecords.filter(function (record) {
    return record.startedAtEpochMs >= startEpochMs && record.startedAtEpochMs < endEpochMs;
  });
  const byResourceType = {};
  const byHost = {};
  const byStatusClass = {};
  let finished = 0;
  let failed = 0;
  let responses = 0;
  let inFlightAtEnd = 0;
  let tileCacheHit = 0;
  let tileCacheMiss = 0;
  selected.forEach(function (record) {
    increment(byResourceType, record.resourceType);
    increment(byHost, record.host);
    if (record.status != null) {
      responses += 1;
      increment(byStatusClass, Math.floor(record.status / 100) + 'xx');
    }
    if (record.failedAtEpochMs != null && record.failedAtEpochMs <= endEpochMs) failed += 1;
    if (record.finishedAtEpochMs != null && record.finishedAtEpochMs <= endEpochMs) finished += 1;
    if (record.tileCache === 'hit') tileCacheHit += 1;
    if (record.tileCache === 'miss') tileCacheMiss += 1;
    if (
      (record.finishedAtEpochMs == null || record.finishedAtEpochMs > endEpochMs) &&
      (record.failedAtEpochMs == null || record.failedAtEpochMs > endEpochMs)
    ) {
      inFlightAtEnd += 1;
    }
  });
  return {
    observable: true,
    count: selected.length,
    responses: responses,
    finished: finished,
    failed: failed,
    inFlightAtEnd: inFlightAtEnd,
    byResourceType: byResourceType,
    byHost: byHost,
    byStatusClass: byStatusClass,
    tileCache: {
      observable: tileCacheHit + tileCacheMiss > 0,
      hit: tileCacheHit,
      miss: tileCacheMiss,
      hitRate: tileCacheHit + tileCacheMiss
        ? Number((tileCacheHit / (tileCacheHit + tileCacheMiss)).toFixed(4))
        : null,
    },
  };
}


function attachRequestSummary(metric, startEpochMs) {
  metric.requests = summarizeRequests(
    startEpochMs != null ? startEpochMs : metric.timeOriginEpochMs + metric.startedAtMs,
    metric.timeOriginEpochMs + metric.endedAtMs
  );
  return metric;
}
