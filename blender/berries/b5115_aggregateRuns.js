// aggregateRuns
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/runtime/benchmark-vector-tuning.mjs, line 472
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


function memoryUsedBytes(run) {
  const memory = run && run.memory && run.memory.afterZoom;
  if (!memory) return null;
  if (Number.isFinite(memory.cdp && memory.cdp.jsHeapUsedBytes)) {
    return memory.cdp.jsHeapUsedBytes;
  }
  if (Number.isFinite(memory.performance && memory.performance.usedJSHeapSize)) {
    return memory.performance.usedJSHeapSize;
  }
  return null;
}


function aggregateRuns(runs, requestedRuns, ssimBaselineIdentity) {
  const successful = runs.filter(function (run) {
    return run.ok;
  });
  const failed = runs.filter(function (run) {
    return !run.ok;
  });
  const frameTimes = successful.flatMap(function (run) {
    return (
      (run.zoom && run.zoom.frames && Array.isArray(run.zoom.frames.samplesMs)
        ? run.zoom.frames.samplesMs
        : [])
    ).filter(Number.isFinite);
  });
  const frameGapDurations = successful.flatMap(function (run) {
    return (
      (run.zoom && run.zoom.frames && Array.isArray(run.zoom.frames.gapSamplesMs)
        ? run.zoom.frames.gapSamplesMs
        : [])
    ).filter(Number.isFinite);
  });
  const longTaskDurations = successful.flatMap(function (run) {
    return (
      (run.zoom && run.zoom.longTasks && Array.isArray(run.zoom.longTasks.samplesMs)
        ? run.zoom.longTasks.samplesMs
        : [])
    ).filter(Number.isFinite);
  });
  const droppedByRun = successful.map(function (run) {
    return Number(run.zoom && run.zoom.frames && run.zoom.frames.droppedFramesEstimate) || 0;
  });
  const gapCounts = successful.map(function (run) {
    return Number(run.zoom && run.zoom.frames && run.zoom.frames.gapCount) || 0;
  });
  const longTaskCounts = successful.map(function (run) {
    return Number(run.zoom && run.zoom.longTasks && run.zoom.longTasks.count) || 0;
  });
  const ssimValues = successful
    .map(function (run) {
      const evidence = run.visual && run.visual.ssim;
      if (ssimBaselineIdentity === null) return null;
      if (
        typeof ssimBaselineIdentity === 'string' &&
        (!evidence || evidence.baselineIdentity !== ssimBaselineIdentity)
      ) {
        return null;
      }
      return evidence && evidence.score;
    })
    .filter(Number.isFinite);
  const droppedTotal = droppedByRun.reduce(function (sum, value) {
    return sum + value;
  }, 0);
  const gapTotal = gapCounts.reduce(function (sum, value) {
    return sum + value;
  }, 0);
  const longTaskTotal = longTaskCounts.reduce(function (sum, value) {
    return sum + value;
  }, 0);
  return {
    requestedRuns: requestedRuns,
    completedRuns: successful.length,
    failedRuns: failed.length,
    complete: successful.length === requestedRuns && failed.length === 0,
    firstIdleMs: statistics(
      successful.map(function (run) {
        return run.firstIdle && run.firstIdle.elapsedMs;
      })
    ),
    zoom: {
      frameTimeMs: statistics(frameTimes),
      frameGapMs: statistics(frameGapDurations),
      frameGapCountTotal: gapTotal,
      frameGapCountPerRun: successful.length ? rounded(gapTotal / successful.length) : null,
      droppedFramesTotal: droppedTotal,
      droppedFramesPerRun: successful.length
        ? rounded(droppedTotal / successful.length)
        : null,
      longTaskDurationMs: statistics(longTaskDurations),
      longTaskCountTotal: longTaskTotal,
      longTaskCountPerRun: successful.length
        ? rounded(longTaskTotal / successful.length)
        : null,
    },
    memory: {
      usedJSHeapBytes: statistics(successful.map(memoryUsedBytes)),
    },
    visualSsim: statistics(ssimValues, 6),
  };
}
