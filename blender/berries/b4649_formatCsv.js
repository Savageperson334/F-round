// formatCsv
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file origami/src/origami/csv.js, line 22
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatCsv(array) {
  if (!array || array.length === 0) {
    return "";
  }

  // Helper to quote field if necessary
  const formatField = (value) => {
    // Convert value to string.
    let field = String(value);

    // RFC 4180: Quote field if it contains a comma, a CR/LF, or a double quote
    if (field.search(/("|,|\n|\r)/) !== -1) {
      // Escape existing double quotes by replacing " with ""
      field = field.replace(/"/g, '""');
      // Surround the field with quotes
      field = `"${field}"`;
    }
    return field;
  };

  // Extract header fields from the first object.
  const headerFields = Object.keys(array[0]);

  // Generate the header row by formatting each header field.
  const headerRow = headerFields.map(formatField).join(",");

  // Map through each object and generate a CSV row.
  const dataRows = array.map((row) => {
    return headerFields
      .map((field) => formatField(row[field] !== undefined ? row[field] : ""))
      .join(",");
  });

  // Concatenate header and data rows, joining and ending with CRLF.
  return [headerRow, ...dataRows].join("\r\n") + "\r\n";
}
