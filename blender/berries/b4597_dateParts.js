// dateParts
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file async-tree/src/drivers/CalendarMap.js, line 85
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function dateParts(date) {
  let year;
  let month;
  let day;
  if (typeof date === "string") {
    const parts = date.split("-");
    year = parts[0] ? parseInt(parts[0]) : undefined;
    month = parts[1] ? parseInt(parts[1]) : undefined;
    day = parts[2] ? parseInt(parts[2]) : undefined;

    if (
      (year && isNaN(year)) ||
      (month && isNaN(month)) ||
      (day && isNaN(day))
    ) {
      throw new TypeError(`Tree.calendar: invalid date: ${date}`);
    }
  }
  return { year, month, day };
}
