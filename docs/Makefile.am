#
# If this is a distribution tarball, the "html" and "man" dirs should
# be here already.  And we never want to delete them (because they
# came distributed with the tarball).
#
# If this is a git clone, these directories will be generated on the
# fly, and should be deleted as part of "make clean".

SPHINXBUILD ?= sphinx-build
PYTHON3      = $(or $(shell which python3), $(shell which python))

man_pages = \
        MPI_Abort.3 \
        MPI_Bcast.3 \
        mpirun.1

man_page_sources = $(addprefix src/, $(addsuffix .rst, $(man_pages)))

docs_sources = \
        src/index.rst \
        src/configuring.rst \
        src/building.rst \
        src/man_pages.rst

# Putting the directory names "build/html" and "build/man" in the
# EXTRA_DIST targets means that Automake will effectively invoke "make
# build/html" and "make build/man" as part of "make dist", which will
# conveniently fail if sphinx-build is not available.  Specifically:
# it'll fail to make a tarball if you don't have Sphinx.
EXTRA_DIST = \
        $(docs_sources) \
        $(man_page_sources) \
        src/conf.py \
        sphinx-requirements.txt \
        build/html \
        build/man

dist_man_MANS =
BUILT_SOURCES =

if DOCS_CAN_BUILD
# We don't install the HTML docs
BUILT_SOURCES += build/html
# We don't need to list the man pages here (see below)
endif # DOCS_CAN_BUILD

if DOCS_CAN_INSTALL
# This will implicitly cause the man pages to be built, too
# JMS Automake won't parse "$(addprefix build/man, $(man_pages))" --
# temporarily list all the man pages here until we figure out
# something better.  Grumble.
dist_man_MANS += \
        build/man/MPI_Abort.3 \
        build/man/MPI_Bcast.3 \
        build/man/mpirun.1
endif # DOCS_CAN_INSTALL

build/html: build/html/index.html
# This is a token man page that will cause all the rest to get generated.
build/man: build/man/MPI_Abort.3

if DOCS_CAN_BUILD
build/html/index.html: $(docs_sources) $(man_page_sources) src/conf.py
	$(SPHINXBUILD) -b html "$(srcdir)/src" "$(builddir)/build/html"

build/man/MPI_Abort.3: $(man_page_sources) src/conf.py
	$(SPHINXBUILD) -b man "$(srcdir)/src" "$(builddir)/build/man"

else # DOCS_CAN_BUILD

# Note: we specifically do _not_ make "docs_cannot_build" be a
# dependency, but rather invoke "$(MAKE) docs_cannot_build" only if
# the target files do not exist and make decides that we need to build
# it.
build/html/index.html:
	$(MAKE) docs_cannot_build
build/man/openmpi.1:
	$(MAKE) docs_cannot_build

.PHONY: docs_cannot_build
docs_cannot_build:
	@ echo " "
	@ echo "ERROR: configure determined that we cannot build/install the docs"
	@ echo "ERROR: cannot continue"
	@ echo " "
	@ false

endif # DOCS_CAN_BUILD

maintainer-clean-local:
	-rm -rf build
	-rm -rf $(DOCS_TARGETS)
