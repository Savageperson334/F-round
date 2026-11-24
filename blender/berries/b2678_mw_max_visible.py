# mw_max_visible
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/milky_way.py, line 107
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mw_max_visible(lat: float) -> int:
    """
    Return the maximum number of MW waypoints that can ever be visible
    (peak altitude ≥ 10°) from the given latitude.

    Uses the nominal declinations of the 14 catalog waypoints.
    """
    # Nominal decs from gal_to_radec at each l, b=0 (pre-computed)
    # Order matches _MW_WAYPOINT_ORDER
    _WAYPOINT_DECS = [
        -28.9,  # Galactic Core          l=0°,   b=0°
         -6.6,  # Scutum Star Cloud      l=27°,  b=-3°
        +10.7,  # Aquila Rift            l=45°,  b=0°
        +41.3,  # Cygnus Star Cloud      l=80°,  b=+1°
        +60.4,  # Cepheus Cloud          l=105°, b=+3°
        +59.6,  # Cassiopeia/Perseus     l=135°, b=-1°
        +28.9,  # Galactic Anticenter    l=180°, b=0°
         +1.7,  # Monoceros              l=210°, b=-2°
        -28.2,  # Puppis Star Cloud      l=245°, b=0°
        -46.5,  # Vela Supernova Region  l=265°, b=-3°
        -59.7,  # Carina Nebula & Cloud  l=287°, b=-1°
        -62.9,  # Crux & Coalsack        l=302°, b=0°
        -53.9,  # Norma Star Cloud       l=330°, b=-2°
        -40.9,  # Scorpius Star Cloud    l=347°, b=-2°
    ]
    return sum(1 for dec in _WAYPOINT_DECS if 90 - abs(lat - dec) >= 10)
