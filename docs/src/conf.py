# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

import datetime

# "project", "author", and "copyright" are Sphinx config variables.
_year     = datetime.date.today().year
project   = 'Open MPI'
author    = 'The Open MPI Community'
copyright = f'{_year}, {author}'

# Some versions of Sphinx changed the default value of this param
# (cough cough 4.0.0 and 4.0.1).  Set it specifically to the value
# that we want: False (i.e., don't generate man pages in
# man/<SECTION>/ subdirectories).
man_make_section_directory = False

# Read the Open MPI version data from the VERSION file.
# Yes, "../VERSION" works correctly, even with VPATH builds.  :-)
with open(f"../../VERSION") as fp:
    ompi_lines = fp.readlines()

ompi_data = dict()
for ompi_line in ompi_lines:
    if '#' in ompi_line:
        ompi_line, _ = ompi_line.split("#")
    ompi_line = ompi_line.strip()

    if '=' not in ompi_line:
        continue

    ompi_key, ompi_val = ompi_line.split("=")
    ompi_data[ompi_key.strip()] = ompi_val.strip()

# "release" and "version" are sphinx config variables -- assign them
# to the computed Open MPI version number.
_major_minor = f"{ompi_data['major']}.{ompi_data['minor']}"
series       = f"{_major_minor}.x"
release      = f"{_major_minor}.{ompi_data['release']}{ompi_data['greek']}"
version      = release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sphinx_rtd_theme
extensions = ['recommonmark', "sphinx_rtd_theme"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['html', 'man', 'Thumbs.db', '.DS_Store', 'venv']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'


# -- Options for man page output ---------------------------------------------

man_pages = [('MPI_Abort.3', 'MPI_Abort', 'Abort MPI applications', author, 3),
             ('MPI_Bcast.3', 'MPI_Bcast', 'Send a broadcast', author, 3),
             ('mpirun.1', 'mpirun', 'Launch Open MPI applications', author, 1),
             ]

# -- Open MPI-specific options -----------------------------------------------

# The contents of "rst_prolog" are included in every file.  Put common stuff here.

rst_prolog = f"""
.. |mdash|  unicode:: U+02014 .. Em dash
.. |rarrow| unicode:: U+02192 .. Right arrow

.. |ompi_ver| replace:: {release}
.. |ompi_series| replace:: {series}
"""
