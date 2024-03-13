/* neobox_lib.h */
/*
  NEOBOX - A Godot platform targeting single board computers
  Copyright (c) 2017-2023  Emanuele Fornara
  SPDX-License-Identifier: MIT
 */

#ifndef NEOBOX_LIB_H
#define NEOBOX_LIB_H

#ifdef __cplusplus
extern "C" {
#endif

void neobox_parse_neobox_args(int argc, char *argv[]);
int neobox_godot_main(int argc, char *argv[]);

#ifdef __cplusplus
}
#endif

#endif /* NEOBOX_LIB_H */
