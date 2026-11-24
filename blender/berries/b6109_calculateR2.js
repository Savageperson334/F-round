// calculateR2
//
// Copied verbatim from https://github.com/ugun-byte/BioFoundry-PlantTwin
//   file scratch/scientific_benchmark_validation.js, line 71
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Plants and growth models
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function calculateR2(simulatedArr, groundTruthArr) {
  const n = simulatedArr.length;
  const meanY = groundTruthArr.reduce((a, b) => a + b, 0) / n;
  let ssTot = 0;
  let ssRes = 0;
  for (let i = 0; i < n; i++) {
    ssTot += Math.pow(groundTruthArr[i] - meanY, 2);
    ssRes += Math.pow(groundTruthArr[i] - simulatedArr[i], 2);
  }
  return 1 - (ssRes / ssTot);
}
