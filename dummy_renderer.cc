// dummy_renderer.cc
/*
  NEOBOX - A Godot platform targeting single board computers
  Copyright (c) 2017-2023  Emanuele Fornara
  SPDX-License-Identifier: MIT
 */

#include "platform/neobox/custom_renderer.h"

#include <stdio.h>

#include "servers/rendering/dummy/rasterizer_dummy.h"

namespace example {

class Renderer : public neobox::CustomRenderer {
public:
	Renderer() {
		fprintf(stderr, "warning: overriding opengl3 with dummy.\n");
	}
public: // neobox::CustomRenderer
	void make_current() override {
		::RasterizerDummy::make_current();
	}
};

} // namespace example

namespace neobox {

CustomRenderer *new_CustomRenderer() {
	return new example::Renderer();
}

} // namespace neobox
