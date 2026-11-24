# getFileInfo
#
# Copied verbatim from https://github.com/felixriese/thermal-image-processing
#   file tiprocessing/IRUtils.py, line 434
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Metrology, microscopes and geology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def getFileInfo(filename: str):
    """Get file information from filename.

    Parameters
    ----------
    filename : str
        Filename of CSV file

    Returns
    -------
    date : str
        Date of the file
    time : str
        Time of the file
    folder : str
        Measurement folder of the file
    filenumber : str
        Number of the measurement

    Example
    -------
    path = ir_export_20170815_P0000004_005_10-50-08
    date = 20170815
    time = 10-50-08
    folder = P0000004
    filenumber = 005

    """
    date = filename[10:18]
    time = filename[-12:-4]
    folder = filename[19:27]
    filenumber = filename[28:31]

    return date, time, folder, filenumber
