// This file is part of OpenCV project.
// It is subject to the license terms in the LICENSE file found in the top-level directory
// of this distribution and at http://opencv.org/license.html.

#ifndef OPENCV_CORE_SIMD_INTRINSICS_HPP
#define OPENCV_CORE_SIMD_INTRINSICS_HPP

/**
Helper header to support SIMD intrinsics (universal intrinsics) in user code.
Intrinsics documentation: https://docs.opencv.org/master/df/d91/group__core__hal__intrin.html


Checks of target CPU instruction set based on compiler definitions don't work well enough.
More reliable solutions require utilization of configuration systems (like CMake).

So, probably you need to specify your own configuration.

You can do that via CMake in this way:
    add_definitions(/DOPENCV_SIMD_CONFIG_HEADER=opencv_simd_config_custom.hpp)
or
    add_definitions(/DOPENCV_SIMD_CONFIG_INCLUDE_DIR=1)

Additionally you may need to add include directory to your files:
    include_directories("${CMAKE_CURRENT_LIST_DIR}/opencv_config_${MYTARGET}")

These files can be pre-generated for target configurations of your application
or generated by CMake on the fly (use CMAKE_BINARY_DIR for that).

Notes:
- H/W capability checks are still responsibility of your application
- runtime dispatching is not covered by this helper header
*/

#ifdef __OPENCV_BUILD
#error "Use core/hal/intrin.hpp during OpenCV build"
#endif

#ifdef OPENCV_HAL_INTRIN_HPP
#error "core/simd_intrinsics.hpp must be included before core/hal/intrin.hpp"
#endif

#include "../../opencv2/core/cvdef.h"
#include "../../opencv2/core/version.hpp"

#ifdef OPENCV_SIMD_CONFIG_HEADER
#include CVAUX_STR(OPENCV_SIMD_CONFIG_HEADER)
#elif defined(OPENCV_SIMD_CONFIG_INCLUDE_DIR)
#include "opencv_simd_config.hpp"  // corresponding directory should be added via -I compiler parameter
#else  // custom config headers

#if (!defined(CV_AVX_512F) || !CV_AVX_512F) && (defined(__AVX512__) || defined(__AVX512F__))
#  include <immintrin.h>
#  undef CV_AVX_512F
#  define CV_AVX_512F 1
#  ifndef OPENCV_SIMD_DONT_ASSUME_SKX  // Skylake-X with AVX-512F/CD/BW/DQ/VL
#    undef CV_AVX512_SKX
#    define CV_AVX512_SKX 1
#    undef CV_AVX_512CD
#    define CV_AVX_512CD 1
#    undef CV_AVX_512BW
#    define CV_AVX_512BW 1
#    undef CV_AVX_512DQ
#    define CV_AVX_512DQ 1
#    undef CV_AVX_512VL
#    define CV_AVX_512VL 1
#  endif
#endif // AVX512

// GCC/Clang: -mavx2
// MSVC: /arch:AVX2
#if defined __AVX2__
#  include <immintrin.h>
#  undef CV_AVX2
#  define CV_AVX2 1
#  if defined __F16C__
#    undef CV_FP16
#    define CV_FP16 1
#  endif
#endif

#endif

// SSE / NEON / VSX is handled by cv_cpu_dispatch.h compatibility block
#include "cv_cpu_dispatch.h"

#include "hal/intrin.hpp"

#endif // OPENCV_CORE_SIMD_INTRINSICS_HPP
