# overflying
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/genesis.py, line 157
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

_COUNTRIES = ['United Kingdom', 'Europe', 'Europe', 'Europe', 'Japan', 'Asia', 'Asia', 'Asia', 'Saudi Arabia', 'Russia',
              'Russia', 'Russia', 'the Indian Ocean', 'the Indian Ocean', 'Oceania', 'Africa', 'the Atlantic Ocean',
              'the Atlantic Ocean', 'the Atlantic Ocean', 'Greenland', 'South America', 'South America',
              'Central America', 'North America', 'North America', 'North America', 'Antartica', 'the Pacific Ocean',
              'the Pacific Ocean', 'the Pacific Ocean', 'the Pacific Ocean', 'the Artic Ocean', 'the Artic Ocean',
              'the Artic Ocean']

_PI = 3.1415926535898

_ZONES = [(54, -4, 7), (42, -4, 6), (48, 16, 12), (64, 18, 7), (36, 139, 11), (10, 115, 23), (27, 98, 27), (32, 61, 23),
          (24, 44, 12), (60, 151, 19), (62, 103, 19), (57, 53, 17), (-21, 80, 35), (-50, 40, 20), (-22, 134, 26),
          (0, 17, 38), (-40, -14, 27), (-48, -39, 18), (33, -37, 23), (71, -37, 12), (-8, -59, 24), (-40, -65, 19),
          (16, -88, 17), (47, -97, 30), (63, -151, 8), (72, -98, 10), (-90, 0, 22), (17, -173, 47), (-25, -128, 47),
          (-49, 142, 28), (-38, -165, 34), (90, 140, 10), (90, 60, 8), (90, 168, 8)]


def overflying(lat, lon):
    for (latc, lonc, rc), name in zip(_ZONES, _COUNTRIES):
        rc_km = rc * (_PI / 180) * 6371
        dlat = (lat - latc) * (_PI / 180) / 2.0
        dlon = (lon - lonc) * (_PI / 180) / 2.0
        a = math.sin(dlat) * math.sin(dlat) + math.cos(latc * (_PI / 180)) * math.cos(lat * (_PI / 180)) * \
            math.sin(dlon) * math.sin(dlon)
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        if 6371 * c <= rc_km:
            return 'Flying over %s' % name
    return 'The overflown area is not found in the database'
