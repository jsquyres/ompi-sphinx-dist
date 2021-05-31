#
# If this is a distribution tarball, the "html" and "man" dirs should
# be here already.  And we never want to delete them (because they
# came distributed with the tarball).
#
# If this is a git clone, these directories will be generated on the
# fly, and should be deleted as part of "make clean".

SPHINXBUILD ?= sphinx-build
PYTHON3      = $(or $(shell which python3), $(shell which python))
VENVDIR      = $(top_builddir)/docs/ompi-docs-venv

RST_SOURCE = \
        index.rst \
        configuring.rst \
        building.rst \
        MPI_Abort.3.rst \
        MPI_Bcast.3.rst

# Putting the directory names "html" and "man" in the EXTRA_DIST
# targets (via $(DOCS_TARGETS) means that Automake will effectively
# invoke "make html" and "make man" as part of "make dist", which will
# conveniently fail if sphinx-build is not available.  Specifically:
# it'll fail to make a tarball if you don't have Sphinx.
EXTRA_DIST = \
        $(RST_SOURCE) \
        conf.py \
        sphinx-requirements.txt \
        html \
        man

man_MANS =
BUILT_SOURCES =

if DOCS_CAN_BUILD
# We don't install the HTML docs
BUILT_SOURCES += html
# We don't need to list the man pages here (see below)
endif # DOCS_CAN_BUILD

if DOCS_CAN_INSTALL
# This will implicitly cause the man pages to be built, too
man_MANS += man/openmpi.1
endif # DOCS_CAN_INSTALL

# Simple rule to make a Python virtual environment and install Sphinx
# in it.  This doesn't have to be how Sphinx is installed; it's just
# an option for developers who want to use it.
ompi-docs-venv:
	$(PYTHON3) -m venv $(VENVDIR)
	. ./$(VENVDIR)/bin/activate && pip3 --disable-pip-version-check install -r sphinx-requirements.txt

html: html/index.html
man: man/openmpi.1

if DOCS_CAN_BUILD
html/index.html: $(RST_SOURCE) $(DOCS_VENV_TARGET)
	@ $(MAKE) run_sphinx TYPE=html

man/openmpi.1: $(RST_SOURCE) $(DOCS_VENV_TARGET)
	@ $(MAKE) run_sphinx TYPE=man

# If there's a venv dir present, activate before running Sphinx.
run_sphinx:
	@if test -r $(VENVDIR)/bin/activate; then \
	    . ./$(VENVDIR)/bin/activate && \
	        $(SPHINXBUILD) -M $(TYPE) "$(srcdir)" "$(builddir)"; \
	 else \
	    $(SPHINXBUILD) -M $(TYPE) "$(srcdir)" "$(builddir)"; \
	 fi

else # DOCS_CAN_BUILD

# Note: we specifically do _not_ make "docs_cannot_build" be a
# dependency, but rather invoke "$(MAKE) docs_cannot_build" only if
# the target files do not exist and make decides that we need to build
# it.
html/index.html:
	$(MAKE) docs_cannot_build
man/openmpi.1:
	$(MAKE) docs_cannot_build

.PHONY: docs_cannot_build
docs_cannot_build:
	@ echo " "
	@ echo "ERROR: configure determined that we cannot build/install the docs"
	@ echo "ERROR: cannot continue"
	@ echo " "
	@ false

endif # DOCS_CAN_BUILD

distclean-local:
	-rm -rf $(VENVDIR)

maintainer-clean-local:
	-rm -rf html man doctrees
	-rm -rf $(DOCS_TARGETS)
