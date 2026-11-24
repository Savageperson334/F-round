// setCell
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/conditions/table.js, line 56
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const isFiniteNumber = (value) => typeof value === 'number' && Number.isFinite(value)


function columnValues(table, header) {
  const values = table?.columns?.[header]
  return (table?.times || []).map((_, index) =>
    isFiniteNumber(values?.[index]) ? values[index] : null
  )
}


function setCell(table, header, index, value) {
  const values = columnValues(table, header)
  values[index] = isFiniteNumber(value) ? value : null
  return { ...table, columns: { ...table.columns, [header]: values } }
}
