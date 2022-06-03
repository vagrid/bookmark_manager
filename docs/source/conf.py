# -*- coding: utf-8 -*-
# 
# Bookmark manager documentation build configuration file,
# created by sphinx-quickstart Sun May 29 10:16:20 2022.

# ==========
# Path setup
# ==========

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import bookmark_manager

# =====================
# General configuration
# =====================

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
                "sphinx.ext.autodoc",
                "sphinx.ext.autosummary",
                "sphinx.ext.intersphinx",
                "sphinx.ext.todo",
                "numpydoc",
#                "nbsphinx",
             ]

# ===================
# Project information
# ===================

project   = bookmark_manager.__title__
copyright = bookmark_manager.__copyright__
author    = bookmark_manager.__author__

# =======
# Version
# =======

# The version information for the project being documenting
# The short X.Y version.
version  = bookmark_manager.__version__
# The full version, including alpha/beta/rc tags.
release  = bookmark_manager.__version__




# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
