# SP1
#
# Copied verbatim from https://github.com/LiquidFun/Simple-Traffic-Simulation
#   file Datenauswertung/signalprogramme.py, line 51
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

BLINKEN = "BLINKEN"

DUNKEL = "DUNKEL"

GRUEN = "GRÜN"

ROT = "ROT"

GELB = "GELB"

R_G = "ROT_GELB"


def dxSchaltung(t,go,stop,x):
	if go<=stop:
		if t >= go and t < stop: return x
	else:
		if t >= go or t < stop: return x
	return DUNKEL


def r_gggSchaltung(t,begin,go,stop,end):
	if begin<=go:
		if t >= begin and t < go: return R_G
	else:
		if t >= begin or t < go: return R_G

	if go<=stop:
		if t >= go and t < stop: return GRUEN
	else:
		if t >= go or t < stop: return GRUEN

	if stop<=end:
		if t >= stop and t < end: return GELB
	else:
		if t >= stop or t < end: return GELB

	return ROT


def rgSchaltung(t,go,stop):
	if go<=stop:
		if t >= go and t < stop: return GRUEN
	else:
		if t >= go or t < stop: return GRUEN
	return ROT


def SP1(t):
	s = {}
	s["K1"] = r_gggSchaltung(t,34,35,71,74)
	s["K2"] = r_gggSchaltung(t,86,87,6,9)
	s["K3"] = r_gggSchaltung(t,14,15,69,72)
	s["K4"] = s["K2"]
	s["K7"] = r_gggSchaltung(t,13,14,25,28)
	s["S2"] = r_gggSchaltung(t,16,18,24,28)
	s["B4"] = dxSchaltung(t,80,85,GRUEN)
	s["FA11"] = rgSchaltung(t,79,9)
	s["FA13"] = s["FA11"]
	s["F2"] = rgSchaltung(t,14,69)
	s["FA31"] = rgSchaltung(t,79,6)
	s["FA33"] = s["FA31"]
	s["F41"] = rgSchaltung(t,34,69)
	s["F43"] = dxSchaltung(t,12,34,ROT)
	s["BL13,14"] = dxSchaltung(t,78,14,BLINKEN)
	s["BL21"] = dxSchaltung(t,18,81,BLINKEN)
	s["BL22"] = dxSchaltung(t,33,81,BLINKEN)
	s["BL33,34"] = s["BL13,14"]
	s["BL41"] = dxSchaltung(t,33,79,BLINKEN)
	s["BLS21,22"] = DUNKEL
	s["K1_TK2"] = r_gggSchaltung(t,34,35,10,13)
	s["S1_TK2"] = r_gggSchaltung(t,15,17,24,28)
	s["F4_TK2"] = rgSchaltung(t,34,8)
	s["BL42_TK2"] = dxSchaltung(t,33,11,BLINKEN)
	return s
