// custom_renderer.h
/*
  NEOBOX - A Godot platform targeting single board computers
  Copyright (c) 2017-2023  Emanuele Fornara
  SPDX-License-Identifier: MIT
 */

#ifndef NEOBOX_CUSTOM_RENDERER_H
#define NEOBOX_CUSTOM_RENDERER_H

namespace neobox {

struct CustomRenderer {
	virtual ~CustomRenderer();
	virtual void make_current() = 0;
};

CustomRenderer *new_CustomRenderer();

} // namespace neobox

#endif // NEOBOX_CUSTOM_RENDERER_H
