// getBorderStyleObject
//
// Copied verbatim from https://github.com/raphamorim/origami.js
//   file src/utilities.js, line 45
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function normalizeStyle(style) {
  if (!style)
    style = {};

  var borderSize = (style.borderSize || null),
    borderColor = (style.borderColor || null),
    borderStyle = (style.borderStyle || []);

  if (style.border) {
    var border = [],
      borderString = style.border;

    // 0 - Size: [0-9]px
    border = border.concat(style.border.match(/[0-9]*\.?[0-9]px?/i));
    borderString = borderString.replace(/[0-9]*\.?[0-9]px?/i, '');

    // 1 - Style
    border = border.concat(borderString.match(/solid|dashed|dotted/i));
    borderString = borderString.replace(/solid|dashed|dotted/i, '');

    // 2 - Color
    border = border.concat(borderString.match(/[^\s]+/i));

    if (!borderSize)
      borderSize = border[0];
    if (!borderColor)
      borderColor = border[2];

    borderStyle = border[1];
  }

  if (borderSize)
    borderSize = borderSize.replace(/[^0-9]/g, '');

  if (typeof(borderStyle) === 'string') {
    if (borderStyle === 'dashed')
      borderStyle = [12];
    else if (borderStyle === 'dotted')
      borderStyle = [3];
    else
      borderStyle = [];
  }

  style['borderSize'] = borderSize;
  style['borderStyle'] = borderStyle;
  style['borderColor'] = borderColor;
  return style;
}


function getBorderStyleObject(prop) {
  return normalizeStyle({border: prop});
}
