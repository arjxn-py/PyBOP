# Configuration file for the Sphinx documentation builder.


# -- Path setup --------------------------------------------------------------
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_path)

from pybop.version import __version__  # noqa: E402

# -- Project information -----------------------------------------------------
project = "PyBOP"
copyright = "2023, The PyBOP Team"
author = "The PyBOP Team"
release = f"v{__version__}"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinx_copybutton",
    "autoapi.extension",
    # custom extentions
    "_extension.gallery_directive",
    # For extension examples and demos
    "myst_parser",
    "sphinx_favicon",
]

templates_path = ["_templates"]
autoapi_template_dir = "_templates/autoapi"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for autoapi -------------------------------------------------------
autoapi_type = "python"
autoapi_dirs = ["../pybop"]
autoapi_keep_files = True
autoapi_root = "api"
autoapi_member_order = "groupwise"

# -- Options for HTML output -------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_show_sourcelink = False
html_title = "PyBOP Documentation"

# html_theme options
html_theme_options = {
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/pybop/",
            "icon": "fa-custom fa-pypi",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/pybop-team/pybop",
            "icon": "fab fa-github-square",
        },
    ],
    "search_bar_text": "Search the docs...",
    "show_prev_next": False,
}

html_static_path = ["_static"]
html_js_files = ["custom-icon.js"]
