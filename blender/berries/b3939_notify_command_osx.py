# notify_command_osx
#
# Copied verbatim from https://github.com/wzpan/MusicBoxApi
#   file MusicBoxApi/utils.py, line 24
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def notify_command_osx(msg, msg_type, t=None):
    command = '/usr/bin/osascript -e "display notification \\\"{}\\\" {} with title \\\"musicbox\\\""'
    sound = 'sound name \\\"/System/Library/Sounds/Ping.aiff\\\"' if msg_type else ''
    return command.format(msg, sound)
