// makeLookupEntry
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/layer/table.js, line 147
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const setState = (states, t, key) => {
	// convert the key into an array of integers (0, 1, 2)
	const characters = Array.from(key).map((char) => parseInt(char, 10));

	// filter out the keys which do not below in this set.
	// the reason we aren't doing this ahead of time is because it requires
	// parsing each character, which we are already doing here.
	// only keys with the number of "0"s matching the number "t" are allowed.
	if (characters.filter((x) => x === 0).length !== t) {
		return;
	}

	// initialize the result to false (no solution possible).
	// eslint-disable-next-line no-param-reassign
	states[t][key] = false;

	// solution will either be true, false, or an array of two integers
	// where the two integers describe a modification to be made.
	// if we encounter a valid suggestion (modify one character takes us
	// to a valid state), store it here.
	const modifications = [];

	// iterate through every character (only the zero characters),
	// replace it with a 1 and a 2 and see if either lead us to a valid solution.
	for (let i = 0; i < characters.length; i += 1) {
		const roundModifications = [];

		// look at the unknown layers only (where the character is zero)
		if (characters[i] !== 0) {
			continue;
		}

		// in place of the unknowns, try each of the possible states (1, 2)
		for (let x = 1; x <= 2; x += 1) {
			// temporarily modify the character in place to our guess
			characters[i] = x;

			// if this state exists in the previous set, save the modification
			// instruction which would lead our key to this next key.
			if (states[t - 1][characters.join("")] !== false) {
				roundModifications.push([i, x]);
			}
		}

		// undo our guess, set it back to 0, in preparation for the next iteration
		characters[i] = 0;

		// if we found a modifications instruction (even if we aren't using them),
		// we can say the solution is no longer false. now we just need to know if
		// the solution will be a modification instruction or simply "true".
		if (roundModifications.length) {
			// eslint-disable-next-line no-param-reassign
			states[t][key] = true;
		}

		// if roundModifications is length 2, this means both possible states
		// led us to a solution, therefore we can't infer anything.
		// only add a modification instruction if this round found only 1.
		if (roundModifications.length === 1) {
			modifications.push(roundModifications[0]);
		}
	}

	// if found, the result will be the (first) modification instruction.
	// it doesn't matter which one, we just need one.
	if (modifications.length) {
		// eslint-disable-next-line no-param-reassign
		states[t][key] = [modifications[0][0], modifications[0][1]];
	}
};


const makeLookupEntry = (valid_states) => {
	// the choose count can be inferred by the length of the valid states
	// (assuming they are all the same length)
	const chooseCount = valid_states[0].length;

	// this array will contain all states (keys) and their solutions (values).
	// the states are sorted into arrays of objects, where keys are sorted by
	// how many 0s they contain (index [0]: no zeros, index [1]: 1 zero...)
	/** @type {{[key: string]: (boolean | [number, number])}[]} */
	const states = Array.from(Array(chooseCount + 1)).map(() => ({}));

	// this array initializer will create all permutations of 1s and 2s (no zeros)
	// all strings having the length of chooseCount. (ie. for 6: 111112, 212221)
	// because all these keys contain no zeros, they are all inside the [0] index.
	// initialize all keys to "false" for now.
	Array.from(Array(2 ** chooseCount))
		.map((_, i) => i.toString(2))
		.map((str) =>
			Array.from(str)
				.map((n) => parseInt(n, 10) + 1)
				.join(""),
		)
		.map((str) => `11111${str}`.slice(-chooseCount))
		.forEach((key) => {
			states[0][key] = false;
		});

	// set all valid cases to be "true" (indicating the solution is possible)
	valid_states.forEach((s) => {
		states[0][s] = true;
	});

	// now we fill in the rest of the states. In a similar manner as before,
	// create all permuations, length of chooseCount, but this time include
	// 0, 1, or 2 for every character. "t" relates to the number of unknowns
	// (number of zeros) this will be the index in "states" we store this key.
	// level [0] is already complete, start incrementing from level [1].
	// this is generating, for every level, the same set of strings, which is
	// too much, however they will get filtered out inside setState.
	Array.from(Array(chooseCount))
		.map((_, i) => i + 1)
		.map((t) =>
			Array.from(Array(3 ** chooseCount))
				.map((_, i) => i.toString(3))
				.map((str) => `000000${str}`.slice(-chooseCount))
				.forEach((key) => setState(states, t, key)),
		);

	// gather all solutions together into one object.
	/** @type {{[key: string]: Readonly<(boolean | [number, number])>}} */
	const lookup = states.reduce((a, b) => ({ ...a, ...b }));

	// recursively freeze result, this is intended to be an immutable reference
	Object.keys(lookup)
		.filter((key) => typeof lookup[key] === "object")
		.forEach((key) => {
			lookup[key] = Object.freeze(lookup[key]);
		});
	return Object.freeze(lookup);
};
