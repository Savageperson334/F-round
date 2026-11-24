# rgSchaltung
#
# Copied verbatim from https://github.com/LiquidFun/Simple-Traffic-Simulation
#   file Datenauswertung/signalprogramme.py, line 36
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

GRUEN = "GRÜN"

ROT = "ROT"


def rgSchaltung(t,go,stop):
	if go<=stop:
		if t >= go and t < stop: return GRUEN
	else:
		if t >= go or t < stop: return GRUEN
	return ROT
