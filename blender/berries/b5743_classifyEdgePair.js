// classifyEdgePair
//
// Copied verbatim from https://github.com/rabbit-ear/rabbit-ear
//   file src/layer/tacosTortillas.js, line 26
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const classifyEdgePair = (edgePairFacesSide) => {
	// a taco means both faces of an edge are on the same side
	const isTaco = edgePairFacesSide.map(([f0, f1]) => f0 === f1);

	// break each case into taco-taco, tortilla-tortilla, or taco-tortilla

	// both edges are tacos. taco-taco is the only case where it might result as
	// invalid. taco-taco is only valid if both tacos are on the same side.
	if (isTaco[0] && isTaco[1]) {
		if (edgePairFacesSide[0][0] !== edgePairFacesSide[1][0]) {
			return 0;
		}
		return 1;
	}

	// both are tortillas. all cases are valid.
	// if the tortilla's are aligned meaning both tortilla's index 0
	// are on top of each other, the result is 2, otherwise 3.
	if (!isTaco[0] && !isTaco[1]) {
		return edgePairFacesSide[0][0] === edgePairFacesSide[1][0] ? 2 : 3;
	}

	// taco-tortilla. all cases are valid.
	// depending on the taco-position, result is either 4/5 or 6/7
	// for the taco, which side (+1/-1) are its faces on?
	const tacoSide = isTaco[0] ? edgePairFacesSide[0][0] : edgePairFacesSide[1][0];

	// get the tortilla's facesSides array
	const tortillaFacesSide = isTaco[0] ? edgePairFacesSide[1] : edgePairFacesSide[0];

	// is the taco on top of the [0] index of the tortilla or the [1] index?
	const tortillaSideMatch = tacoSide === tortillaFacesSide[0] ? 0 : 1;
	const whichIsTaco = isTaco[0] ? 0 : 2;
	return 4 + whichIsTaco + tortillaSideMatch;
};
