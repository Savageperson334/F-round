# waveform_id_to_network_station_location
#
# Copied verbatim from https://github.com/seisbench/seisbench
#   file seisbench/util/trace_ops.py, line 101
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def waveform_id_to_network_station_location(waveform_id):
    """
    Takes a waveform_id as string in the format Network.Station.Location.Channel and
    returns a string with channel dropped. If the waveform_id does not conform to the format,
    the input string is returned.

    :param waveform_id: Waveform ID in format Network.Station.Location.Channel
    :type waveform_id: str
    :return: Waveform ID in format Network.Station.Location
    :rtype: str
    """
    parts = waveform_id.split(".")
    if len(parts) != 4:
        return waveform_id
    else:
        return ".".join(parts[:-1])
