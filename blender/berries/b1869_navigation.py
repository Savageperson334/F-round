# navigation
#
# Copied verbatim from https://github.com/fenderberg/fm1-sy1
#   file tools/make_site.py, line 65
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

PAGES = (("", "Overview"), ("emu", "Play"), ("editor", "Synth Editor"), ("manager", "Patch Manager"),
         ("install", "Install"), ("manual", "Manual"), ("news", "What's new"))

SOURCE = "https://github.com/fenderberg/fm1-sy1"


def navigation(current, up):
    links = []
    for route, label in PAGES:
        href = up + (route + "/" if route else "") or "./"
        active = ' aria-current="page"' if route == current.split("/")[0] else ""
        if route == "manager" and not active:    # the manager is an app: it gets its own tab
            active = ' target="_blank" rel="noopener"'
        links.append(f'<a href="{href}"{active}><span class="nav-led" aria-hidden="true"></span>{label}</a>')
    links.append(f'<a href="{SOURCE}" class="source-link">Source <span aria-hidden="true">↗</span></a>')
    return ('<a class="site-skip" href="#content">Skip to content</a>\n'
            '<header class="site-header"><div class="site-header-inner">'
            f'<a class="site-brand" href="{up or "./"}" aria-label="SY1 home">SY<span>1</span>'
            '<span class="brand-caption">VIRTUAL ANALOG<br>FOR THE FM-1</span></a>'
            '<nav class="site-nav" aria-label="Main navigation">' + "".join(links) + '</nav></div></header>')
