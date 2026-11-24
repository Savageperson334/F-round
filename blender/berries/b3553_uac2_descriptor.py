# uac2_descriptor
#
# Copied verbatim from https://github.com/rolkinn/capstan
#   file tools/teensy_msc/patch.py, line 172
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def uac2_descriptor(speed):
    """The audio function (USB Audio Class 2.0) for one speed: 2 stereo channels (Master L/R)
    to the computer, 2 stereo channels from it; one fixed 44.1 kHz clock; no controls."""
    hs = speed == "480"
    tx_ch = "AUDIO_TX_CHANNELS_%s" % speed
    tx_config = "0x03,0,0,0"                                 # (2: front left, right stereo)
    tx_names = "0"
    interval = "1" if hs else "1"                            # data: every microframe (high speed) / frame
    fb_interval = "4" if hs else "1"                         # feedback: every 1 ms
    fb_size = "4" if hs else "3"                             # USB 2.0 5.12.4.2 / Apple TN3190: 4 B (16.16) HS, 3 B (10.14) FS
    return """#if defined(AUDIO_UAC2) // L7_UAC2: tools/teensy_msc/patch.py
        // interface association: the audio function, UAC2 (protocol 0x20), iFunction = 2 (product name "Capstan")
        8, 11, AUDIO_INTERFACE, 3, 0x01, 0x00, 0x20, 2,
        // AudioControl interface (iInterface = 2)
        9, 4, AUDIO_INTERFACE, 0, 0, 0x01, 0x01, 0x20, 2,
        // class-specific AC header: UAC 2.00, category I/O box, wTotalLength 75 (the AC descriptors), no controls
        9, 0x24, 0x01, 0x00, 0x02, 0x08, 75, 0, 0x00,
        // clock source: internal, fixed; frequency and validity readable
        8, 0x24, 0x0A, AUDIO_CLOCK_ID, 0x01, 0x05, 0, 0,
        // input terminal 1 (line connector): what goes to the computer (iTerminal = 2)
        17, 0x24, 0x02, 1, 0x03, 0x06, 0, AUDIO_CLOCK_ID, %(tx_ch)s, %(tx_config)s, %(tx_names)s, 0x00, 0x00, 2,
        // output terminal 2 (USB streaming): to the computer (iTerminal = 2)
        12, 0x24, 0x03, 2, 0x01, 0x01, 0, 1, AUDIO_CLOCK_ID, 0x00, 0x00, 2,
        // input terminal 3 (USB streaming): from the computer (iTerminal = 2)
        17, 0x24, 0x02, 3, 0x01, 0x01, 0, AUDIO_CLOCK_ID, AUDIO_RX_CHANNELS, 0x03, 0, 0, 0, 0, 0x00, 0x00, 2,
        // output terminal 4 (line connector): into Capstan (iTerminal = 2)
        12, 0x24, 0x03, 4, 0x03, 0x06, 0, 3, AUDIO_CLOCK_ID, 0x00, 0x00, 2,
        // AudioStreaming interface: to the computer, alternate 0 (idle)
        9, 4, AUDIO_INTERFACE+1, 0, 0, 0x01, 0x02, 0x20, 2,
        // alternate 1: streaming
        9, 4, AUDIO_INTERFACE+1, 1, 1, 0x01, 0x02, 0x20, 2,
        // AS general: terminal 2, PCM
        16, 0x24, 0x01, 2, 0x00, 0x01, 0x01, 0, 0, 0, %(tx_ch)s, %(tx_config)s, %(tx_names)s,
        // format type I: 2-byte subslots, 16 bits
        6, 0x24, 0x02, 0x01, 2, 16,
        // endpoint: isochronous, asynchronous, data (IN)
        7, 5, AUDIO_TX_ENDPOINT | 0x80, 0x05, LSB(AUDIO_TX_SIZE_%(speed)s), MSB(AUDIO_TX_SIZE_%(speed)s), %(interval)s,
        // class-specific endpoint
        8, 0x25, 0x01, 0x00, 0x00, 0, 0, 0,
        // AudioStreaming interface: from the computer, alternate 0 (idle)
        9, 4, AUDIO_INTERFACE+2, 0, 0, 0x01, 0x02, 0x20, 2,
        // alternate 1: streaming, with the feedback endpoint
        9, 4, AUDIO_INTERFACE+2, 1, 2, 0x01, 0x02, 0x20, 2,
        // AS general: terminal 3, PCM, stereo
        16, 0x24, 0x01, 3, 0x00, 0x01, 0x01, 0, 0, 0, AUDIO_RX_CHANNELS, 0x03, 0, 0, 0, 0,
        // format type I: 2-byte subslots, 16 bits
        6, 0x24, 0x02, 0x01, 2, 16,
        // endpoint: isochronous, asynchronous, data (OUT)
        7, 5, AUDIO_RX_ENDPOINT, 0x05, LSB(AUDIO_RX_SIZE_%(speed)s), MSB(AUDIO_RX_SIZE_%(speed)s), %(interval)s,
        // class-specific endpoint
        8, 0x25, 0x01, 0x00, 0x00, 0, 0, 0,
        // feedback endpoint (IN): the rate Capstan wants
        7, 5, AUDIO_SYNC_ENDPOINT | 0x80, 0x11, %(fb_size)s, 0, %(fb_interval)s,
#else
""" % dict(tx_ch=tx_ch, tx_config=tx_config, tx_names=tx_names, interval=interval,
           fb_interval=fb_interval, fb_size=fb_size, speed=speed)
