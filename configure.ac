# -*- shell-script -*-

AC_INIT([ompi-sphinx-dist], [0.5.0], [https://example.com])
AC_PREREQ(2.60)
AC_CONFIG_AUX_DIR(config)
AC_CONFIG_MACRO_DIR(config)

AC_CANONICAL_HOST
AC_CANONICAL_TARGET

AM_INIT_AUTOMAKE([foreign subdir-objects no-define 1.13.4 tar-ustar])
AM_SILENT_RULES([yes])

AC_PROG_CC_C99

AC_ENABLE_SHARED
AC_DISABLE_STATIC

LT_INIT
LT_OUTPUT

abs_builddir=`pwd`
cd $srcdir
abs_srcdir=`pwd`
cd "$abs_builddir"

# Can we build the docs?
#
# - If $with_docs_venv==yes, then assume yes
# - If we can find sphinx-build in our path and find all of the
#   required pip modules, then yes
# - Otherwise, no

# This result is used below (in some cases)
AC_PATH_PROG([SPHINX_BUILD], [sphinx-build])

AC_MSG_CHECKING([if we can build the docs])
DOCS_CAN_BUILD=0
AS_IF([test "$with_docs_venv" = "yes"],
      [DOCS_CAN_BUILD=1],
      [AS_IF([test -z "SPHINX_BUILD"],
             [AC_MSG_RESULT([no (cannot find sphinx-build executable)])],
             [ # Check for the Python modules we need
              missing_modules=
              for line in `egrep -v '^#' $abs_srcdir/docs/sphinx-requirements.txt`; do
                  pip_module=`echo $line | cut -d= -f1`
                  python_module=`echo $pip_module | sed 's/-/_/g'`
                  echo "Testing python import of: $python_module" >&5
                  python3 -c "import $python_module" >&5 2>&5
                  st=$?
                  AS_IF([test $st -ne 0],
                        [missing_modules="$pip_module $missing_modules"])
              done
              AS_IF([test -n "$missing_modules"],
                    [msg=`echo $missing_modules`
                     AC_MSG_RESULT([no (missing pip modules: $msg)])],
                    [DOCS_CAN_BUILD=1])
             ])
      ])
AM_CONDITIONAL(DOCS_CAN_BUILD, [test $DOCS_CAN_BUILD -eq 1])

# We already printed the different "no" results, but we didn't print
# "yes".
AS_IF([test $DOCS_CAN_BUILD -eq 1], [AC_MSG_RESULT([yes])])

# Are we *installing* the docs?
#
# - If we're able to build the docs, yes
# - If the docs/html and docs/man directories already exist (i.e., a
#   distribution tarball), yes
# - Otherwise, no

AC_MSG_CHECKING([if docs are already present])
DOCS_ALREADY_PRESENT=0
AS_IF([test -d $abs_srcdir/docs/html && test -d $abs_srcdir/docs/man],
      [DOCS_ALREADY_PRESENT=1])
AS_IF([test $DOCS_ALREADY_PRESENT -eq 1],
      [AC_MSG_RESULT([yes])],
      [AC_MSG_RESULT([no])])

AC_MSG_CHECKING([if we will install the docs])
DOCS_CAN_INSTALL=0
AS_IF([test $DOCS_CAN_BUILD -eq 1 || test $DOCS_ALREADY_PRESENT -eq 1],
      [DOCS_CAN_INSTALL=1])
AM_CONDITIONAL(DOCS_CAN_INSTALL, [test $DOCS_CAN_INSTALL -eq 1])

AS_IF([test $DOCS_CAN_INSTALL -eq 1],
      [AC_MSG_RESULT([yes])],
      [AC_MSG_RESULT([no])])

# Provide --enable-install-docs CLI option.  This option will cause
# configure to fail/abort if we cannot install the docs.  This is
# expected to be useful for people who cannot use an
# automatically-created Python virtual environment (e.g., if you're on
# a machine not connected to the internet, and "pip install ..." will
# fail).
AC_ARG_ENABLE([install-docs],
              [AS_HELP_STRING([--enable-install-docs],
                              [Cause configure to fail/abort if we cannot install the docs.  This option is typically only useful in builds from git clones (where the docs are not already built).])])
AS_IF([test $DOCS_CAN_INSTALL -eq 0 && test "$enable_install_docs" = "yes"],
      [AC_MSG_WARN([--enable-install-docs was specified,])
       AC_MSG_WARN([but configure cannot figure out how to build or install the docs])
       AC_MSG_ERROR([Cannot continue])])

#########################

AC_CONFIG_FILES([
        Makefile
        config/Makefile
        src/Makefile
        docs/Makefile
])
AC_OUTPUT
