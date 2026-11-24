# addRect
#
# Copied verbatim from https://github.com/rsandler00/plotly-scientific-plots
#   file plotly_scientific_plots/plot_subcomponents.py, line 98
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def addRect(start, end, orientation='V', color='#ff0000', opacity=0.1, name='rect'):
    ''' This makes a rectangluar background from start til end with shaded color. Useful for highlighting things in plots'''
    if orientation == 'V':
        xref = 'x'
        yref = 'paper'
        x0 = start
        x1 = end
        y0 = 0
        y1 = 1
    elif orientation == 'H':
        yref = 'y'
        xref = 'paper'
        y0 = start
        y1 = end
        x0 = 0
        x1 = 1
    else:
        raise ValueError('Orientation must be either "H" or "V". You input %s' % str(orientation))

    return {
        'type': 'rect',
        'xref': xref,
        'yref': yref,
        'x0': x0,
        'y0': y0,
        'x1': x1,
        'y1': y1,
        'fillcolor': color,
        'opacity': opacity,
        'line': {
            'width': 0,
        },
        'path': str(name)
    }
