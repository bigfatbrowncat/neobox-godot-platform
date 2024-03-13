// neobox.cc
/*
  NEOBOX - A Godot platform targeting single board computers
  Copyright (c) 2017-2023  Emanuele Fornara
  SPDX-License-Identifier: MIT
 */

#include "neobox.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdarg.h>

#define NEOBOX_VERSION "2.1.0"
#define NEOBOX_STATUS "stable"

static void print_msg(const char *format, va_list ap) {
	fprintf(stderr, "neobox: ");
	vfprintf(stderr, format, ap);
	fprintf(stderr, "\n");
}

namespace neobox {

void warn(const char *format, ...) {
	va_list ap;
	va_start(ap, format);
	print_msg(format, ap);
	va_end(ap);
}

void fatal(const char *format, ...) {
	va_list ap;
	va_start(ap, format);
	print_msg(format, ap);
	va_end(ap);
	exit(1);
}

extern const char *commit_id;
extern const char *license;

} // namespace neobox

#include "neobox_lib.h"

static void usage(const char *program_name, int code) {
	printf("\n"
		"usage: %s [godot args] [--neobox [options]]\n"
		"\n"
		"options:\n"
		"  -v                  show version and exit\n"
		"  -l                  show license and exit\n"
		"  -h                  show this page and exit\n"
	"\n", program_name);
	exit(code);
}

extern "C" void neobox_parse_neobox_args(int argc, char *argv[]) {
	const char *program_name = argv[0];
	for (int i = 1; i < argc; i++) {
		const char *s = argv[i];
		if (!strcmp(s, "-v")) {
			printf("%s.%s.%s\n", NEOBOX_VERSION, NEOBOX_STATUS, neobox::commit_id);
			exit(0);
		} else if (!strcmp(s, "-l")) {
			puts(neobox::license);
			exit(0);
		} else if (!strcmp(s, "-h")) {
			usage(program_name, 0);
		} else {
			usage(program_name, 1);
		}
	}
}
