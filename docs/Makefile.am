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

help:
	@$(SPHINXBUILD) -M help "$(srcdir)" "$(builddir)"

man_MANS = man/openmpi.1

# Simple rule to make a Python virtual environment and install Sphinx
# in it.  This doesn't have to be how Sphinx is installed; it's just
# an option for developers who want to use it.
venv: Makefile
	virtualenv --python=$(PYTHON3) $(VENVDIR)
	. ./$(VENVDIR)/bin/activate && pip install -r sphinx-requirements.txt

# If there's a venv, activate it before invoking Sphinx.
html man: Makefile $(RST_SOURCE)
	@if test -d $(VENVDIR)/bin/activate/; then \
	    . ./$(VENVDIR)/bin/activate; \
	 fi; \
	 $(SPHINXBUILD) -M $@ "$(srcdir)" "$(builddir)"

.PHONY: html
.PHONY: man

clean-local:
	rm -rf \
	    "$(builddir)/html" \
	    "$(builddir)/man" \
	    "$(builddir)/doctrees"

distclean-local:
	rm -rf $(VENVDIR)
