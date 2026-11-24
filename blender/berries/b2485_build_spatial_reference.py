# build_spatial_reference
#
# Copied verbatim from https://github.com/jordan-zav/GeoRefMaps
#   file app/export.py, line 30
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Maps, forgotten infrastructures and borders
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def build_spatial_reference(mode: str, utm_zone: str) -> dict:
    if mode == "geographic":
        return {
            "mode": "geographic",
            "crs_name": "WGS 84",
            "epsg": 4326,
        }

    zone_to_epsg = {
        "17S": 32717,
        "18S": 32718,
        "19S": 32719,
    }
    return {
        "mode": "projected",
        "crs_name": f"WGS 84 / UTM zone {utm_zone}",
        "utm_zone": utm_zone,
        "epsg": zone_to_epsg.get(utm_zone),
    }
