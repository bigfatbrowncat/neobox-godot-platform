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
      CC="${CC}" \
      CXX="${CXX}" \
      LD="${CXX}" $1
