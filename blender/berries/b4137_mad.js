// mad
//
// Copied verbatim from https://github.com/Agerbi-Nouha/beehive-monitoring-app
//   file backend/src/utils/soundBaseline.js, line 10
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function median(values) {
  const nums = values.filter((v) => typeof v === 'number').sort((a, b) => a - b);
  if (!nums.length) return null;
  const mid = Math.floor(nums.length / 2);
  return nums.length % 2 === 0 ? (nums[mid - 1] + nums[mid]) / 2 : nums[mid];
}


function mad(values, med) {
  const m = typeof med === 'number' ? med : median(values);
  if (typeof m !== 'number') return null;
  const deviations = values.filter((v) => typeof v === 'number').map((v) => Math.abs(v - m));
  const madVal = median(deviations);
  if (typeof madVal !== 'number') return null;
  // Convert MAD to std-like sigma (for normal dist) for easier interpretation
  return madVal * 1.4826;
}
