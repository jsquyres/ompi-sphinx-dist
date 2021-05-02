# -*- shell-script -*-

AC_INIT([ompi-sphinx-dist], [0.5.0], [https://example.com], [osd])
AC_PREREQ(2.60)
AC_CONFIG_AUX_DIR(config)
AC_CONFIG_MACRO_DIR(config)

AC_CANONICAL_HOST
AC_CANONICAL_TARGET

AM_INIT_AUTOMAKE([foreign dist-bzip2 subdir-objects no-define 1.13.4 tar-ustar])
AM_SILENT_RULES([yes])

AC_PROG_CC_C99

AC_ENABLE_SHARED
AC_DISABLE_STATIC

LT_INIT
LT_OUTPUT

AC_CONFIG_FILES([
	Makefile
	config/Makefile
	src/Makefile
	docs/Makefile
])
AC_OUTPUT
