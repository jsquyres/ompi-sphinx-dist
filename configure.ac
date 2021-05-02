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

AC_PATH_PROG([SPHINX_BUILD], [sphinx-build])
AS_IF([test -z "$SPHINX_BUILD"],
    [AC_MSG_WARN([Cannot find sphinx-build executable in your PATH])

     dnl If you do not already have the HTML docs/man pages built
     dnl (e.g., this is a git clone) and you do not have sphinx-build,
     dnl then you will not be able to build them.  Distribution
     dnl tarballs will have the HTML docs/man pages built already, so
     dnl this won't be an issue.
     AS_IF([test ! -r $srcdir/docs/html/index.html],
         [AC_MSG_WARN([You will not be able to build the Open MPI HTML documentation])])
     AS_IF([test ! -r $srcdir/docs/man/openmpi.1],
         [AC_MSG_WARN([You will not be able to build the Open MPI man page documentation])])
    ])

AC_CONFIG_FILES([
        Makefile
        config/Makefile
        src/Makefile
        docs/Makefile
])
AC_OUTPUT
