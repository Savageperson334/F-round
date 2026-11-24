# ERSI_url_builder
#
# Copied verbatim from https://github.com/mnky9800n/Python-course-materials-for-seismology-students
#   notebook example_notebooks/cartopy/Plotting a pretty map using cartopy.ipynb (its code cells joined in order; line 195 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ERSI_url_builder(llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat):

    ''' This function returns a url for querying the ArcGIS
    ESRI satellite image database based on the lower left
    coordinate and upper right coordinate provided.''' 

    url = 'http://server.arcgisonline.com/ArcGIS/rest/services/ESRI_Imagery_World_2D/MapServer/export?bbox=%.2f,%.2f,%.2f,%.2f&bboxSR=4269&imageSR=4269&size=2000,2200&dpi=96&format=png32&f=image' % (llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat)

    return url
