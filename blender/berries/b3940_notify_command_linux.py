# notify_command_linux
#
# Copied verbatim from https://github.com/wzpan/MusicBoxApi
#   file MusicBoxApi/utils.py, line 30
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def notify_command_linux(msg, t=None):
    command = '/usr/bin/notify-send "' + msg + '"'
    if t:
        command += ' -t ' + str(t)
    command += ' -h int:transient:1'
    return command
