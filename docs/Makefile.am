#
# If this is a distribution tarball, the "html" and "man" dirs should
# be here already.  And we never want to delete them (because they
# came distributed with the tarball).
#
# If this is a git clone, these directories will be generated on the
# fly, and should be deleted as part of "make clean".

SPHINXBUILD ?= sphinx-build
PYTHON3      = $(or $(shell which python3), $(shell which python))
VENVDIR      = venv

RST_SOURCE = \
        index.rst \
        configuring.rst \
        building.rst \
        MPI_Abort.3.rst \
        MPI_Bcast.3.rst

# Putting "html" and "man" in the EXTRA_DIST targets means that
# Automake will effectively invoke "make html" and "make man" as part
# of "make dist", which will conveniently fail if sphinx-build is not
# available.  Specifically: it'll fail to make a tarball if you don't
# have Sphinx.
EXTRA_DIST = \
        $(RST_SOURCE) \
        conf.py \
        sphinx-requirements.txt \
        html \
        man

man_MANS = \
        man/openmpi.1

# Simple rule to make a Python virtual environment and install Sphinx
# in it.  This doesn't have to be how Sphinx is installed; it's just
# an option for developers who want to use it.
venv:
	virtualenv --python=$(PYTHON3) $(VENVDIR)
	. ./$(VENVDIR)/bin/activate && pip install -r sphinx-requirements.txt

html: html/index.html
html/index.html: $(RST_SOURCE)
	@if test -d $(VENVDIR)/bin/activate/; then \
	    . ./$(VENVDIR)/bin/activate; \
	 fi; \
	 $(SPHINXBUILD) -M html "$(srcdir)" "$(builddir)"

man: man/openmpi.1
man/openmpi.1: $(RST_SOURCE)
	@if test -d $(VENVDIR)/bin/activate/; then \
	    . ./$(VENVDIR)/bin/activate; \
	 fi; \
	 $(SPHINXBUILD) -M man "$(srcdir)" "$(builddir)"

maintainer-clean-local:
	-rm -rf html man doctrees
	-rm -rf $(VENVDIR)
