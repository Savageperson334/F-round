// getModes
//
// Copied verbatim from https://github.com/IceCreamYou/THREE.Terrain
//   file src/analysis.js, line 599
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Procedural and generated worlds
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function bucketNumbersLinearly(data, bucketCount, min, max) {
    var i = 0,
        l = data.length;
    // If min and max aren't given, set them to the highest and lowest data values
    if (typeof min === 'undefined') {
        min = Infinity;
        max = -Infinity;
        for (i = 0; i < l; i++) {
            if (data[i] < min) min = data[i];
            if (data[i] > max) max = data[i];
        }
    }
    
    // Ensure min and max are different
    if (min === max) {
        max = min + 1;  // Prevent division by zero
    }
    
    var inc = (max - min) / bucketCount,
        buckets = new Array(bucketCount);
    // Initialize buckets
    for (i = 0; i < bucketCount; i++) {
        buckets[i] = [];
    }
    // Put the numbers into buckets
    for (i = 0; i < l; i++) {
        // Clamp data to min/max range
        var value = Math.max(min, Math.min(max, data[i]));
        
        // Buckets include the lower bound but not the higher bound, except the top bucket
        if (value === max) {
            buckets[bucketCount-1].push(value);
        } else {
            var bucketIndex = Math.floor((value - min) / inc);
            // Safety check for index
            bucketIndex = Math.max(0, Math.min(bucketCount - 1, bucketIndex));
            buckets[bucketIndex].push(value);
        }
    }
    return buckets;
}


function getModes(data, bucketCount, min, max) {
    // Handle empty data
    if (!data || data.length === 0) {
        return [];
    }
    
    // Ensure min and max are different
    if (min === max) {
        max = min + 1;
    }
    
    var buckets = bucketNumbersLinearly(data, bucketCount, min, max),
        maxLen = 0,
        modes = [];
    
    // Find the buckets with the most values
    for (var i = 0, l = buckets.length; i < l; i++) {
        if (buckets[i].length > maxLen) {
            maxLen = buckets[i].length;
            modes = [min + ((i + 0.5) / bucketCount) * (max - min)];
        }
        else if (buckets[i].length === maxLen && maxLen > 0) {
            modes.push(min + ((i + 0.5) / bucketCount) * (max - min));
        }
    }
    
    // If no modes were found (all buckets empty), return empty array
    if (modes.length === 0) {
        return [];
    }
    
    // Round modes to integers if they're close enough to integers
    for (var j = 0; j < modes.length; j++) {
        if (Math.abs(modes[j] - Math.round(modes[j])) < 0.001) {
            modes[j] = Math.round(modes[j]);
        } else {
            modes[j] = parseFloat(modes[j].toFixed(3));
        }
    }
    
    return modes;
}
