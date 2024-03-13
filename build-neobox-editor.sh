scons target=editor \
      optimize=speed \
      debug_symbols=no \
      platform=linuxbsd \
      use_llvm=no \
      vulkan=false \
      opengl3=true \
      openxr=false \
      use_volk=false \
      tools=no \
      use_static_cpp=yes \
      -j5 \
      $1

#      frt_std=c++17 \
#      frt_custom_renderer=true \
#      arch=x86_64 \
#      frt_pkg_config="/home/user/projects/recalbox/output/host/bin/pkg-config" \
#      CCFLAGS="-I/home/user/projects/recalbox/output/host/aarch64-buildroot-linux-gnu/sysroot/usr/include" \
#      CXXFLAGS="-flax-vector-conversions" \
#      CC="/home/user/projects/recalbox/output/host/bin/aarch64-buildroot-linux-gnu-gcc" \
#      CXX="/home/user/projects/recalbox/output/host/bin/aarch64-buildroot-linux-gnu-g++" \
#      LD="/home/user/projects/recalbox/output/host/bin/aarch64-buildroot-linux-gnu-g++" \
