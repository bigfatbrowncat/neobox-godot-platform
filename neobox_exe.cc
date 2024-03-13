// neobox_exe.cc
/*
  NEOBOX - A Godot platform targeting single board computers
  Copyright (c) 2017-2023  Emanuele Fornara
  SPDX-License-Identifier: MIT
 */

#include "neobox_lib.h"

#include <string.h>

static void handle_neobox_args(int *argc, char ***argv) {
	for (int i = 1; i < *argc; i++) {
		if (!strcmp((*argv)[i], "--neobox")) {
			(*argv)[i] = (*argv)[0];
			int neobox_argc = *argc - i;
			char **neobox_argv = &(*argv)[i];
			neobox_parse_neobox_args(neobox_argc, neobox_argv);
			*argc = i;
			break;
		}
	}
}

int main(int argc, char *argv[]) {
	handle_neobox_args(&argc, &argv);
	return neobox_godot_main(argc, argv);
}
