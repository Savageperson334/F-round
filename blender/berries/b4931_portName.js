// portName
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file src/place_ports.js, line 4
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function portName(nodeId, edgeId, portName) {
    if (!(nodeId || edgeId))
        return null; // must have one key or the other
    if (nodeId) nodeId = nodeId.replace(/\//g, '%2F');
    if (edgeId) edgeId = edgeId.replace(/\//g, '%2F');
    return `${nodeId ? `node/${nodeId}` : `edge/${edgeId}`}/${portName}`;
}
