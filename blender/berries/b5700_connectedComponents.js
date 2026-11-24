// connectedComponents
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/graph/connectedComponents.js, line 16
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const connectedComponents = (array_array) => {
	const components = [];
	/** @param {number} index @param {number} currentGroup */
	const recurse = (index, currentGroup) => {
		// FOLD allows null or undefined in _faces arrays
		if (index === null || index === undefined || !(index in array_array)) {
			return 0;
		}
		// only set unset component entries.
		// the return value is only meaningful during the first call to recurse()
		// for each row, meaning, if this row has already been set at time of the
		// first call, then no components have this group index, so, use this group
		// index for the next component and next recursion.
		if (components[index] !== undefined) {
			return 0;
		}

		// set this component to be a member of the current group, and recurse
		// through all of its adjacent components, setting every adjacent
		// component to be a member of this group. in this case do nothing with
		// the return value of recurse().
		components[index] = currentGroup;
		array_array[index].forEach((i) => recurse(i, currentGroup));

		// this group number has been applied to one or more components,
		// return and tell the main loop to use the next group index for the
		// next set of components and their recursion.
		return 1;
	};

	// iterate through every row, increment the group index only if one or more
	// components were set to this group, so we don't skip any numbers.
	for (let row = 0, group = 0; row < array_array.length; row += 1) {
		// allow arrays with holes
		if (!(row in array_array)) {
			continue;
		}
		group += recurse(row, group);
	}
	return components;
};
