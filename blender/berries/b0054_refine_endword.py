# refine_endword
#
# Copied verbatim from https://github.com/Anush-DP/Handwriting-recognition
#   notebook load_test.ipynb (its code cells joined in order; line 208 of those)
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def refine_endword(array):
	refine_list = []
	for y in range(len(array)-1):
		if array[y]+1 < array[y+1]:
			refine_list.append(array[y])
	refine_list.append(array[-1])
	return refine_list
