# unicode_normalize
#
# Copied verbatim from https://github.com/nishimotz/libkuraji
#   file src/libkuraji/unicodeutil.py, line 89
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Braille and tactile information
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import unicodedata

_POST_NFKC_MAP = str.maketrans(
	{
		"−": "-",  # minus sign
		"¥": "\\",  # yen sign
		"〜": "~",  # wave dash
		# accented Latin letters folded to ASCII
		"À": "A", "Á": "A", "Â": "A", "Ä": "A", "Å": "A", "Æ": "AE",
		"Ç": "C", "È": "E", "É": "E", "Ê": "E", "Ë": "E",
		"Ì": "I", "Í": "I", "Î": "I", "Ï": "I", "Ñ": "N",
		"Ò": "O", "Ó": "O", "Ô": "O", "Ö": "O", "Ø": "O",
		"Ù": "U", "Ú": "U", "Û": "U", "Ü": "U", "Ý": "Y",
		"à": "a", "á": "a", "â": "a", "ä": "a", "å": "a", "æ": "ae",
		"ç": "c", "è": "e", "é": "e", "ê": "e", "ë": "e",
		"ì": "i", "í": "i", "î": "i", "ï": "i", "ñ": "n",
		"ò": "o", "ó": "o", "ô": "o", "ö": "o", "ø": "o",
		"ù": "u", "ú": "u", "û": "u", "ü": "u", "ý": "y", "ÿ": "y",
		"Œ": "OE", "œ": "oe", "Ÿ": "Y",
	},
)

_PRE_NFKC_MAP = str.maketrans(
	{
		" ": " ",  # no-break space
		" ": " ",  # en space
		" ": " ",  # em space
		" ": " ",  # three-per-em space
		" ": " ",  # four-per-em space
		" ": " ",  # six-per-em space
		" ": " ",  # figure space
		" ": " ",  # punctuation space
		" ": " ",  # thin space
		" ": " ",  # hair space
		# ​ (zero width space) is kept: used as the tab placeholder
		"‎": "",  # left-to-right mark
		"‏": "",  # right-to-left mark
		"�": "",  # replacement character
		# converted to fullwidth by Mecab_text2mecab(); NFKC cannot restore it
		"．": ".",  # fullwidth full stop
	},
)


def unicode_normalize(s: str) -> str:
	if s.isascii():
		# every folded character is non-ASCII and NFKC is the identity
		# for ASCII, so nothing to do
		return s
	s = unicodedata.normalize("NFKC", s.translate(_PRE_NFKC_MAP))
	return s.translate(_POST_NFKC_MAP)
