import os
import sys
from datetime import datetime


sys.path.insert(0, os.path.abspath('../../geogeometry'))  # Adjust if your library is elsewhere

project = 'GeoGeometry'
copyright = f'{datetime.now().year}, Jorge Martínez & GMT'
author = 'Jorge Martínez'
release = '0.0.5'

html_baseurl = "https://jorgemartinezgmt.github.io/geogeometry-docs/"

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Supports NumPy/Google-style docstrings
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints',
    'sphinx_design',
]

exclude_patterns = []


html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']

templates_path = ["_templates"]

html_css_files = ["custom.css"]
html_show_sourcelink = False

html_sidebars = {
    "index": ["gmt_logo_sidebar.html"],
    "releases/index": ["empty_sidebar.html"]
}

html_theme_options = {
    "logo": {
        "image_light": "_static/geogeometry_logo.svg",
        "image_dark": "_static/geogeometry_logo_dark.svg",
    },

    "github_url": "https://github.com/JorgeMartinezGMT/GeoGeometry",
    "show_prev_next": False,
}

html_title = "%s v%s Manual" % (project, release)
