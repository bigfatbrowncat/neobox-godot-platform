scons target=template_release \
      frt_std=c++17 \
      frt_pkg_config="/home/user/projects/recalbox/output/host/bin/pkg-config" \
      optimize=speed \
      debug_symbols=no \
      platform=frt \
      use_llvm=no \
      vulkan=false \
      opengl3=true \
      openxr=false \
      use_volk=false \
      tools=no \
      use_static_cpp=yes \
      arch=arm64 \
      -j5 \
      CCFLAGS="-I/home/user/projects/recalbox/output/host/aarch64-buildroot-linux-gnu/sysroot/usr/include" \
      CXXFLAGS="-flax-vector-conversions" \
      CC="/home/user/projects/recalbox/output/host/bin/aarch64-buildroot-linux-gnu-gcc" \
      CXX="/home/user/projects/recalbox/output/host/bin/aarch64-buildroot-linux-gnu-g++" \
      LD="/home/user/projects/recalbox/output/host/bin/aarch64-buildroot-linux-gnu-g++" $1

#      frt_custom_renderer=true \
