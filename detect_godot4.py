# detect_godot4.py
#
# NEOBOX - A Godot platform targeting single board computers
# Copyright (c) 2017-2023  Emanuele Fornara
# SPDX-License-Identifier: MIT
#

import os
import sys
import platform
import version

# TODO factor out common bits

def get_opts():
	from SCons.Variables import BoolVariable, PathVariable
	return [
		BoolVariable('use_llvm', 'Use llvm compiler', False),
		BoolVariable('use_lto', 'Use link time optimization', False),
		BoolVariable('use_static_cpp', 'Link libgcc and libstdc++ statically', False),
		('neobox_std', 'C++ standard for neobox itself (no/auto/c++98/...)', 'auto'),
		('neobox_arch', 'Architecture (no/arm32v6/arm32v7/arm64v8/amd64)', 'no'),
		('neobox_cross', 'Cross compilation (no/auto/<triple>)', 'no'),
		BoolVariable('neobox_custom_renderer', 'Use custom renderer', False),
		PathVariable('neobox_pkg_config', 'the path to pkg-config executable', 'pkg-config'),
	]


def get_flags():
	return [
	]

def configure_compiler(env):
	if env['use_llvm']:
		env['CC'] = 'clang'
		env['CXX'] = 'clang++'
		env['LD'] = 'clang++'
		env.extra_suffix += '.llvm'

def configure_lto(env):
	if not env['use_lto']:
		return
	if env['use_llvm']:
		env.Append(CCFLAGS=['-flto=thin'])
		env.Append(LINKFLAGS=['-fuse-ld=lld', '-flto=thin'])
		env['AR'] = 'llvm-ar'
		env['RANLIB'] = 'llvm-ranlib'
	else:
		env.Append(CCFLAGS=['-flto'])
		env.Append(LINKFLAGS=['-flto'])
	env.extra_suffix += '.lto'

def configure_arch(env):
	if env['neobox_arch'] == 'arm32v6':
		env.Append(CCFLAGS=['-march=armv6', '-mfpu=vfp', '-mfloat-abi=hard'])
		env.extra_suffix += '.arm32v6'
	elif env['neobox_arch'] == 'arm32v7':
		env.Append(CCFLAGS=['-march=armv7-a', '-mfpu=neon-vfpv4', '-mfloat-abi=hard'])
		env.extra_suffix += '.arm32v7'
	elif env['neobox_arch'] == 'arm64v8':
		env.Append(CCFLAGS=['-march=armv8-a'])
		env.extra_suffix += '.arm64v8'
	elif env['neobox_arch'] != 'no':
		env.extra_suffix += '.' + env['neobox_arch']

def configure_cross(env):
	if 'neobox_pkg_config' in env:
		env['NEOBOX_PKG_CONFIG'] = env['neobox_pkg_config']
	else:
		env['NEOBOX_PKG_CONFIG'] = 'pkg-config'
	print(env['NEOBOX_PKG_CONFIG'])

	# We are addning libmali here, non optional (probably not the best solution)
	env.Append(LINKFLAGS=['-lmali'])

#	if env['neobox_cross'] == 'no':
#		if 'NEOBOX_PKG_CONFIG' not in env:
#			env['NEOBOX_PKG_CONFIG'] = 'pkg-config'
#			return
#	if env['neobox_cross'] == 'auto':
#		triple = {
#			'arm32v6': 'arm-linux-gnueabihf',
#			'arm32v7': 'arm-linux-gnueabihf',
#			'arm64v8': 'aarch64-linux-gnu',
#			'amd64': 'x86_64-linux-gnu',
#		}[env['neobox_arch']]
#	else:
#		triple = env['neobox_cross']
#	if env['use_llvm']:
#		env.Append(CCFLAGS=['-target', triple])
#		env.Append(LINKFLAGS=['-target', triple])
#	else:
#		env['CC'] = triple + '-gcc'
#		env['CXX'] = triple + '-g++'
#	if 'NEOBOX_PKG_CONFIG' not in env:
#		env['NEOBOX_PKG_CONFIG'] = triple + '-pkg-config'

def configure_target(env):
	pass # use engine default

def configure_misc(env):
    env.Append(CPPPATH=['#platform/neobox'])
    env.Append(CPPFLAGS=['-DUNIX_ENABLED'])
    env.Append(CPPDEFINES=[('_FILE_OFFSET_BITS', 64)])
    if env['vulkan']:
        env.Append(CPPDEFINES=['VULKAN_ENABLED'])
    if env['opengl3']:
        env.Append(CPPDEFINES=['GLES3_ENABLED'])
    env.Append(CPPFLAGS=['-DNEOBOX_ENABLED'])
    env.Append(LIBS=['pthread', 'z', 'dl', 'EGL', 'GLESv2'])  # Added 'EGL' and 'GLESv2' here
    if env['CXX'] == 'clang++':
        env['CC'] = 'clang'
        env['LD'] = 'clang++'
    if env['use_static_cpp']:
        env.Append(LINKFLAGS=['-static-libgcc', '-static-libstdc++'])

def configure(env):
	configure_compiler(env)
	configure_lto(env)
	configure_arch(env)
	configure_cross(env)
	configure_target(env)
	configure_misc(env)
