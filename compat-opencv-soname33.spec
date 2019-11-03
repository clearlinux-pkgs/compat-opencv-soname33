#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : compat-opencv-soname33
Version  : 3.3.1
Release  : 68
URL      : https://github.com/opencv/opencv/archive/3.3.1.tar.gz
Source0  : https://github.com/opencv/opencv/archive/3.3.1.tar.gz
Summary  : Open Source Computer Vision Library
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSD-3-Clause-Clear GPL-2.0 JasPer-2.0 LGPL-2.1 Libpng libtiff
Requires: compat-opencv-soname33-bin = %{version}-%{release}
Requires: compat-opencv-soname33-lib = %{version}-%{release}
Requires: compat-opencv-soname33-license = %{version}-%{release}
Requires: compat-opencv-soname33-python = %{version}-%{release}
Requires: compat-opencv-soname33-python3 = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : buildreq-cmake
BuildRequires : buildreq-mvn
BuildRequires : ccache
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : eigen-dev
BuildRequires : gdal-dev
BuildRequires : glib-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk3-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libva-dev
BuildRequires : libva-intel-driver
BuildRequires : libwebp-dev
BuildRequires : mesa-dev
BuildRequires : numpy
BuildRequires : ocl-icd-dev
BuildRequires : openblas
BuildRequires : opencl-headers-dev
BuildRequires : openjdk11-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(clp)
BuildRequires : pkgconfig(gstreamer-video-1.0)
BuildRequires : pkgconfig(libpng)
BuildRequires : protobuf-dev
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : tbb-dev
BuildRequires : v4l-utils-dev
BuildRequires : zlib-dev
# Suppress generation of debuginfo
%global debug_package %{nil}
Patch1: restrict.patch
Patch2: CVE-2017-17760.patch
Patch3: CVE-2017-18009.patch
Patch4: CVE-2018-5268.patch
Patch5: CVE-2018-5269.patch

%description
A demo of the Java wrapper for OpenCV with two examples:
1) feature detection and matching and
2) face detection.
The examples are coded in Scala and Java.
Anyone familiar with Java should be able to read the Scala examples.
Please feel free to contribute code examples in Scala or Java, or any JVM language.

%package bin
Summary: bin components for the compat-opencv-soname33 package.
Group: Binaries
Requires: compat-opencv-soname33-license = %{version}-%{release}

%description bin
bin components for the compat-opencv-soname33 package.


%package lib
Summary: lib components for the compat-opencv-soname33 package.
Group: Libraries
Requires: compat-opencv-soname33-license = %{version}-%{release}

%description lib
lib components for the compat-opencv-soname33 package.


%package license
Summary: license components for the compat-opencv-soname33 package.
Group: Default

%description license
license components for the compat-opencv-soname33 package.


%package python
Summary: python components for the compat-opencv-soname33 package.
Group: Default
Requires: compat-opencv-soname33-python3 = %{version}-%{release}

%description python
python components for the compat-opencv-soname33 package.


%package python3
Summary: python3 components for the compat-opencv-soname33 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the compat-opencv-soname33 package.


%prep
%setup -q -n opencv-3.3.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567830644
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%cmake .. -DWITH_FFMPEG=OFF -DWITH_1394=OFF -DWITH_GSTREAMER=OFF -DWITH_IPP=OFF -DWITH_JASPER=OFF -DWITH_WEBP=OFF -DWITH_OPENEXR=OFF -DWITH_TIFF=OFF -DENABLE_SSE42=ON -DCMAKE_LIBRARY_PATH=/lib64 -DWITH_TBB=on -DWITH_OPENMP=ON -DWITH_VA=ON -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo -DWITH_GSTREAMER=1 -DINSTALL_PYTHON_EXAMPLES=1  -DCPU_DISPATCH=AVX,AVX2,AVX512
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -march=haswell -mzero-caller-saved-regs=used "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake .. -DWITH_FFMPEG=OFF -DWITH_1394=OFF -DWITH_GSTREAMER=OFF -DWITH_IPP=OFF -DWITH_JASPER=OFF -DWITH_WEBP=OFF -DWITH_OPENEXR=OFF -DWITH_TIFF=OFF -DENABLE_SSE42=ON -DCMAKE_LIBRARY_PATH=/lib64 -DWITH_TBB=on -DWITH_OPENMP=ON -DWITH_VA=ON -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=ReleaseWithDebInfo -DWITH_GSTREAMER=1 -DINSTALL_PYTHON_EXAMPLES=1  -DCPU_DISPATCH=AVX,AVX2,AVX512
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1567830644
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-opencv-soname33
cp 3rdparty/cpufeatures/LICENSE %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/3rdparty_cpufeatures_LICENSE
cp 3rdparty/ffmpeg/license.txt %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/3rdparty_ffmpeg_license.txt
cp 3rdparty/ittnotify/src/ittnotify/LICENSE.BSD %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/3rdparty_ittnotify_src_ittnotify_LICENSE.BSD
cp 3rdparty/ittnotify/src/ittnotify/LICENSE.GPL %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/3rdparty_ittnotify_src_ittnotify_LICENSE.GPL
cp 3rdparty/libjasper/LICENSE %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/3rdparty_libjasper_LICENSE
cp 3rdparty/libjasper/copyright %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/3rdparty_libjasper_copyright
cp 3rdparty/libpng/LICENSE %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/3rdparty_libpng_LICENSE
cp 3rdparty/libtiff/COPYRIGHT %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/3rdparty_libtiff_COPYRIGHT
cp 3rdparty/openexr/LICENSE %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/3rdparty_openexr_LICENSE
cp 3rdparty/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/3rdparty_protobuf_LICENSE
cp LICENSE %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/LICENSE
cp modules/dnn/src/torch/COPYRIGHT.txt %{buildroot}/usr/share/package-licenses/compat-opencv-soname33/modules_dnn_src_torch_COPYRIGHT.txt
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/bin/opencv_annotation
rm -f %{buildroot}/usr/bin/opencv_createsamples
rm -f %{buildroot}/usr/bin/opencv_interactive-calibration
rm -f %{buildroot}/usr/bin/opencv_traincascade
rm -f %{buildroot}/usr/bin/opencv_version
rm -f %{buildroot}/usr/bin/opencv_visualisation
rm -f %{buildroot}/usr/bin/haswell/opencv_version
rm -f %{buildroot}/usr/bin/haswell/opencv_interactive-calibration
rm -f %{buildroot}/usr/bin/haswell/opencv_visualisation
rm -f %{buildroot}/usr/bin/haswell/opencv_annotation
rm -f %{buildroot}/usr/share/OpenCV/OpenCVConfig-version.cmake
rm -f %{buildroot}/usr/share/OpenCV/OpenCVConfig.cmake
rm -f %{buildroot}/usr/share/OpenCV/OpenCVModules-releasewithdebinfo.cmake
rm -f %{buildroot}/usr/share/OpenCV/OpenCVModules.cmake
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_eye.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_eye_tree_eyeglasses.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_frontalcatface.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_frontalcatface_extended.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt2.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_frontalface_alt_tree.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_fullbody.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_lefteye_2splits.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_licence_plate_rus_16stages.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_lowerbody.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_profileface.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_righteye_2splits.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_russian_plate_number.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_smile.xml
rm -f %{buildroot}/usr/share/OpenCV/haarcascades/haarcascade_upperbody.xml
rm -f %{buildroot}/usr/share/OpenCV/lbpcascades/lbpcascade_frontalcatface.xml
rm -f %{buildroot}/usr/share/OpenCV/lbpcascades/lbpcascade_frontalface.xml
rm -f %{buildroot}/usr/share/OpenCV/lbpcascades/lbpcascade_frontalface_improved.xml
rm -f %{buildroot}/usr/share/OpenCV/lbpcascades/lbpcascade_profileface.xml
rm -f %{buildroot}/usr/share/OpenCV/lbpcascades/lbpcascade_silverware.xml
rm -f %{buildroot}/usr/share/OpenCV/valgrind.supp
rm -f %{buildroot}/usr/share/OpenCV/valgrind_3rdparty.supp
rm -f %{buildroot}/usr/include/opencv/cv.h
rm -f %{buildroot}/usr/include/opencv/cv.hpp
rm -f %{buildroot}/usr/include/opencv/cvaux.h
rm -f %{buildroot}/usr/include/opencv/cvaux.hpp
rm -f %{buildroot}/usr/include/opencv/cvwimage.h
rm -f %{buildroot}/usr/include/opencv/cxcore.h
rm -f %{buildroot}/usr/include/opencv/cxcore.hpp
rm -f %{buildroot}/usr/include/opencv/cxeigen.hpp
rm -f %{buildroot}/usr/include/opencv/cxmisc.h
rm -f %{buildroot}/usr/include/opencv/highgui.h
rm -f %{buildroot}/usr/include/opencv/ml.h
rm -f %{buildroot}/usr/include/opencv2/calib3d.hpp
rm -f %{buildroot}/usr/include/opencv2/calib3d/calib3d.hpp
rm -f %{buildroot}/usr/include/opencv2/calib3d/calib3d_c.h
rm -f %{buildroot}/usr/include/opencv2/core.hpp
rm -f %{buildroot}/usr/include/opencv2/core/affine.hpp
rm -f %{buildroot}/usr/include/opencv2/core/base.hpp
rm -f %{buildroot}/usr/include/opencv2/core/bufferpool.hpp
rm -f %{buildroot}/usr/include/opencv2/core/core.hpp
rm -f %{buildroot}/usr/include/opencv2/core/core_c.h
rm -f %{buildroot}/usr/include/opencv2/core/cuda.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda.inl.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/block.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/border_interpolate.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/color.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/common.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/datamov_utils.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/detail/color_detail.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/detail/reduce.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/detail/reduce_key_val.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/detail/transform_detail.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/detail/type_traits_detail.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/detail/vec_distance_detail.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/dynamic_smem.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/emulation.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/filters.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/funcattrib.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/functional.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/limits.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/reduce.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/saturate_cast.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/scan.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/simd_functions.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/transform.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/type_traits.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/utility.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/vec_distance.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/vec_math.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/vec_traits.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/warp.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/warp_reduce.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda/warp_shuffle.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda_stream_accessor.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cuda_types.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cv_cpu_dispatch.h
rm -f %{buildroot}/usr/include/opencv2/core/cv_cpu_helper.h
rm -f %{buildroot}/usr/include/opencv2/core/cvdef.h
rm -f %{buildroot}/usr/include/opencv2/core/cvstd.hpp
rm -f %{buildroot}/usr/include/opencv2/core/cvstd.inl.hpp
rm -f %{buildroot}/usr/include/opencv2/core/directx.hpp
rm -f %{buildroot}/usr/include/opencv2/core/eigen.hpp
rm -f %{buildroot}/usr/include/opencv2/core/fast_math.hpp
rm -f %{buildroot}/usr/include/opencv2/core/hal/hal.hpp
rm -f %{buildroot}/usr/include/opencv2/core/hal/interface.h
rm -f %{buildroot}/usr/include/opencv2/core/hal/intrin.hpp
rm -f %{buildroot}/usr/include/opencv2/core/hal/intrin_cpp.hpp
rm -f %{buildroot}/usr/include/opencv2/core/hal/intrin_neon.hpp
rm -f %{buildroot}/usr/include/opencv2/core/hal/intrin_sse.hpp
rm -f %{buildroot}/usr/include/opencv2/core/hal/intrin_vsx.hpp
rm -f %{buildroot}/usr/include/opencv2/core/ippasync.hpp
rm -f %{buildroot}/usr/include/opencv2/core/mat.hpp
rm -f %{buildroot}/usr/include/opencv2/core/mat.inl.hpp
rm -f %{buildroot}/usr/include/opencv2/core/matx.hpp
rm -f %{buildroot}/usr/include/opencv2/core/neon_utils.hpp
rm -f %{buildroot}/usr/include/opencv2/core/ocl.hpp
rm -f %{buildroot}/usr/include/opencv2/core/ocl_genbase.hpp
rm -f %{buildroot}/usr/include/opencv2/core/opengl.hpp
rm -f %{buildroot}/usr/include/opencv2/core/operations.hpp
rm -f %{buildroot}/usr/include/opencv2/core/optim.hpp
rm -f %{buildroot}/usr/include/opencv2/core/ovx.hpp
rm -f %{buildroot}/usr/include/opencv2/core/persistence.hpp
rm -f %{buildroot}/usr/include/opencv2/core/ptr.inl.hpp
rm -f %{buildroot}/usr/include/opencv2/core/saturate.hpp
rm -f %{buildroot}/usr/include/opencv2/core/softfloat.hpp
rm -f %{buildroot}/usr/include/opencv2/core/sse_utils.hpp
rm -f %{buildroot}/usr/include/opencv2/core/traits.hpp
rm -f %{buildroot}/usr/include/opencv2/core/types.hpp
rm -f %{buildroot}/usr/include/opencv2/core/types_c.h
rm -f %{buildroot}/usr/include/opencv2/core/utility.hpp
rm -f %{buildroot}/usr/include/opencv2/core/utils/logger.hpp
rm -f %{buildroot}/usr/include/opencv2/core/utils/trace.hpp
rm -f %{buildroot}/usr/include/opencv2/core/va_intel.hpp
rm -f %{buildroot}/usr/include/opencv2/core/version.hpp
rm -f %{buildroot}/usr/include/opencv2/core/vsx_utils.hpp
rm -f %{buildroot}/usr/include/opencv2/core/wimage.hpp
rm -f %{buildroot}/usr/include/opencv2/cvconfig.h
rm -f %{buildroot}/usr/include/opencv2/dnn.hpp
rm -f %{buildroot}/usr/include/opencv2/dnn/all_layers.hpp
rm -f %{buildroot}/usr/include/opencv2/dnn/dict.hpp
rm -f %{buildroot}/usr/include/opencv2/dnn/dnn.hpp
rm -f %{buildroot}/usr/include/opencv2/dnn/dnn.inl.hpp
rm -f %{buildroot}/usr/include/opencv2/dnn/layer.details.hpp
rm -f %{buildroot}/usr/include/opencv2/dnn/layer.hpp
rm -f %{buildroot}/usr/include/opencv2/dnn/shape_utils.hpp
rm -f %{buildroot}/usr/include/opencv2/features2d.hpp
rm -f %{buildroot}/usr/include/opencv2/features2d/features2d.hpp
rm -f %{buildroot}/usr/include/opencv2/flann.hpp
rm -f %{buildroot}/usr/include/opencv2/flann/all_indices.h
rm -f %{buildroot}/usr/include/opencv2/flann/allocator.h
rm -f %{buildroot}/usr/include/opencv2/flann/any.h
rm -f %{buildroot}/usr/include/opencv2/flann/autotuned_index.h
rm -f %{buildroot}/usr/include/opencv2/flann/composite_index.h
rm -f %{buildroot}/usr/include/opencv2/flann/config.h
rm -f %{buildroot}/usr/include/opencv2/flann/defines.h
rm -f %{buildroot}/usr/include/opencv2/flann/dist.h
rm -f %{buildroot}/usr/include/opencv2/flann/dummy.h
rm -f %{buildroot}/usr/include/opencv2/flann/dynamic_bitset.h
rm -f %{buildroot}/usr/include/opencv2/flann/flann.hpp
rm -f %{buildroot}/usr/include/opencv2/flann/flann_base.hpp
rm -f %{buildroot}/usr/include/opencv2/flann/general.h
rm -f %{buildroot}/usr/include/opencv2/flann/ground_truth.h
rm -f %{buildroot}/usr/include/opencv2/flann/hdf5.h
rm -f %{buildroot}/usr/include/opencv2/flann/heap.h
rm -f %{buildroot}/usr/include/opencv2/flann/hierarchical_clustering_index.h
rm -f %{buildroot}/usr/include/opencv2/flann/index_testing.h
rm -f %{buildroot}/usr/include/opencv2/flann/kdtree_index.h
rm -f %{buildroot}/usr/include/opencv2/flann/kdtree_single_index.h
rm -f %{buildroot}/usr/include/opencv2/flann/kmeans_index.h
rm -f %{buildroot}/usr/include/opencv2/flann/linear_index.h
rm -f %{buildroot}/usr/include/opencv2/flann/logger.h
rm -f %{buildroot}/usr/include/opencv2/flann/lsh_index.h
rm -f %{buildroot}/usr/include/opencv2/flann/lsh_table.h
rm -f %{buildroot}/usr/include/opencv2/flann/matrix.h
rm -f %{buildroot}/usr/include/opencv2/flann/miniflann.hpp
rm -f %{buildroot}/usr/include/opencv2/flann/nn_index.h
rm -f %{buildroot}/usr/include/opencv2/flann/object_factory.h
rm -f %{buildroot}/usr/include/opencv2/flann/params.h
rm -f %{buildroot}/usr/include/opencv2/flann/random.h
rm -f %{buildroot}/usr/include/opencv2/flann/result_set.h
rm -f %{buildroot}/usr/include/opencv2/flann/sampling.h
rm -f %{buildroot}/usr/include/opencv2/flann/saving.h
rm -f %{buildroot}/usr/include/opencv2/flann/simplex_downhill.h
rm -f %{buildroot}/usr/include/opencv2/flann/timer.h
rm -f %{buildroot}/usr/include/opencv2/highgui.hpp
rm -f %{buildroot}/usr/include/opencv2/highgui/highgui.hpp
rm -f %{buildroot}/usr/include/opencv2/highgui/highgui_c.h
rm -f %{buildroot}/usr/include/opencv2/imgcodecs.hpp
rm -f %{buildroot}/usr/include/opencv2/imgcodecs/imgcodecs.hpp
rm -f %{buildroot}/usr/include/opencv2/imgcodecs/imgcodecs_c.h
rm -f %{buildroot}/usr/include/opencv2/imgcodecs/ios.h
rm -f %{buildroot}/usr/include/opencv2/imgproc.hpp
rm -f %{buildroot}/usr/include/opencv2/imgproc/detail/distortion_model.hpp
rm -f %{buildroot}/usr/include/opencv2/imgproc/hal/hal.hpp
rm -f %{buildroot}/usr/include/opencv2/imgproc/hal/interface.h
rm -f %{buildroot}/usr/include/opencv2/imgproc/imgproc.hpp
rm -f %{buildroot}/usr/include/opencv2/imgproc/imgproc_c.h
rm -f %{buildroot}/usr/include/opencv2/imgproc/types_c.h
rm -f %{buildroot}/usr/include/opencv2/ml.hpp
rm -f %{buildroot}/usr/include/opencv2/ml/ml.hpp
rm -f %{buildroot}/usr/include/opencv2/objdetect.hpp
rm -f %{buildroot}/usr/include/opencv2/objdetect/detection_based_tracker.hpp
rm -f %{buildroot}/usr/include/opencv2/objdetect/objdetect.hpp
rm -f %{buildroot}/usr/include/opencv2/objdetect/objdetect_c.h
rm -f %{buildroot}/usr/include/opencv2/opencv.hpp
rm -f %{buildroot}/usr/include/opencv2/opencv_modules.hpp
rm -f %{buildroot}/usr/include/opencv2/photo.hpp
rm -f %{buildroot}/usr/include/opencv2/photo/cuda.hpp
rm -f %{buildroot}/usr/include/opencv2/photo/photo.hpp
rm -f %{buildroot}/usr/include/opencv2/photo/photo_c.h
rm -f %{buildroot}/usr/include/opencv2/shape.hpp
rm -f %{buildroot}/usr/include/opencv2/shape/emdL1.hpp
rm -f %{buildroot}/usr/include/opencv2/shape/hist_cost.hpp
rm -f %{buildroot}/usr/include/opencv2/shape/shape.hpp
rm -f %{buildroot}/usr/include/opencv2/shape/shape_distance.hpp
rm -f %{buildroot}/usr/include/opencv2/shape/shape_transformer.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/autocalib.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/blenders.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/camera.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/exposure_compensate.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/matchers.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/motion_estimators.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/seam_finders.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/timelapsers.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/util.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/util_inl.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/warpers.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/detail/warpers_inl.hpp
rm -f %{buildroot}/usr/include/opencv2/stitching/warpers.hpp
rm -f %{buildroot}/usr/include/opencv2/superres.hpp
rm -f %{buildroot}/usr/include/opencv2/superres/optical_flow.hpp
rm -f %{buildroot}/usr/include/opencv2/video.hpp
rm -f %{buildroot}/usr/include/opencv2/video/background_segm.hpp
rm -f %{buildroot}/usr/include/opencv2/video/tracking.hpp
rm -f %{buildroot}/usr/include/opencv2/video/tracking_c.h
rm -f %{buildroot}/usr/include/opencv2/video/video.hpp
rm -f %{buildroot}/usr/include/opencv2/videoio.hpp
rm -f %{buildroot}/usr/include/opencv2/videoio/cap_ios.h
rm -f %{buildroot}/usr/include/opencv2/videoio/videoio.hpp
rm -f %{buildroot}/usr/include/opencv2/videoio/videoio_c.h
rm -f %{buildroot}/usr/include/opencv2/videostab.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/deblurring.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/fast_marching.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/fast_marching_inl.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/frame_source.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/global_motion.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/inpainting.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/log.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/motion_core.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/motion_stabilizing.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/optical_flow.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/outlier_rejection.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/ring_buffer.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/stabilizer.hpp
rm -f %{buildroot}/usr/include/opencv2/videostab/wobble_suppression.hpp
rm -f %{buildroot}/usr/lib64/haswell/libopencv_calib3d.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_core.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_dnn.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_features2d.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_flann.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_highgui.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_imgcodecs.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_imgproc.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_ml.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_objdetect.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_photo.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_shape.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_stitching.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_superres.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_video.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_videoio.so
rm -f %{buildroot}/usr/lib64/haswell/libopencv_videostab.so
rm -f %{buildroot}/usr/lib64/libopencv_calib3d.so
rm -f %{buildroot}/usr/lib64/libopencv_core.so
rm -f %{buildroot}/usr/lib64/libopencv_dnn.so
rm -f %{buildroot}/usr/lib64/libopencv_features2d.so
rm -f %{buildroot}/usr/lib64/libopencv_flann.so
rm -f %{buildroot}/usr/lib64/libopencv_highgui.so
rm -f %{buildroot}/usr/lib64/libopencv_imgcodecs.so
rm -f %{buildroot}/usr/lib64/libopencv_imgproc.so
rm -f %{buildroot}/usr/lib64/libopencv_ml.so
rm -f %{buildroot}/usr/lib64/libopencv_objdetect.so
rm -f %{buildroot}/usr/lib64/libopencv_photo.so
rm -f %{buildroot}/usr/lib64/libopencv_shape.so
rm -f %{buildroot}/usr/lib64/libopencv_stitching.so
rm -f %{buildroot}/usr/lib64/libopencv_superres.so
rm -f %{buildroot}/usr/lib64/libopencv_video.so
rm -f %{buildroot}/usr/lib64/libopencv_videoio.so
rm -f %{buildroot}/usr/lib64/libopencv_videostab.so
rm -f %{buildroot}/usr/lib64/pkgconfig/opencv.pc
rm -f %{buildroot}/usr/lib/python2.7/site-packages
rm -f %{buildroot}/usr/lib/python2.7/site-packages/cv2.so
rm -f %{buildroot}/usr/lib/python3.7/site-packages
rm -f %{buildroot}/usr/lib/python3.7/site-packages/cv2.cpython-37m-x86_64-linux-gnu.so
## install_append content
mkdir -p %{buildroot}/usr/lib
mv %{buildroot}/usr/lib64/python*  %{buildroot}/usr/lib
rm -fr %{buildroot}/usr/share/OpenCV/samples/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/haswell/opencv_createsamples
/usr/bin/haswell/opencv_traincascade

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libopencv_calib3d.so.3.3
/usr/lib64/haswell/libopencv_calib3d.so.3.3.1
/usr/lib64/haswell/libopencv_core.so.3.3
/usr/lib64/haswell/libopencv_core.so.3.3.1
/usr/lib64/haswell/libopencv_dnn.so.3.3
/usr/lib64/haswell/libopencv_dnn.so.3.3.1
/usr/lib64/haswell/libopencv_features2d.so.3.3
/usr/lib64/haswell/libopencv_features2d.so.3.3.1
/usr/lib64/haswell/libopencv_flann.so.3.3
/usr/lib64/haswell/libopencv_flann.so.3.3.1
/usr/lib64/haswell/libopencv_highgui.so.3.3
/usr/lib64/haswell/libopencv_highgui.so.3.3.1
/usr/lib64/haswell/libopencv_imgcodecs.so.3.3
/usr/lib64/haswell/libopencv_imgcodecs.so.3.3.1
/usr/lib64/haswell/libopencv_imgproc.so.3.3
/usr/lib64/haswell/libopencv_imgproc.so.3.3.1
/usr/lib64/haswell/libopencv_ml.so.3.3
/usr/lib64/haswell/libopencv_ml.so.3.3.1
/usr/lib64/haswell/libopencv_objdetect.so.3.3
/usr/lib64/haswell/libopencv_objdetect.so.3.3.1
/usr/lib64/haswell/libopencv_photo.so.3.3
/usr/lib64/haswell/libopencv_photo.so.3.3.1
/usr/lib64/haswell/libopencv_shape.so.3.3
/usr/lib64/haswell/libopencv_shape.so.3.3.1
/usr/lib64/haswell/libopencv_stitching.so.3.3
/usr/lib64/haswell/libopencv_stitching.so.3.3.1
/usr/lib64/haswell/libopencv_superres.so.3.3
/usr/lib64/haswell/libopencv_superres.so.3.3.1
/usr/lib64/haswell/libopencv_video.so.3.3
/usr/lib64/haswell/libopencv_video.so.3.3.1
/usr/lib64/haswell/libopencv_videoio.so.3.3
/usr/lib64/haswell/libopencv_videoio.so.3.3.1
/usr/lib64/haswell/libopencv_videostab.so.3.3
/usr/lib64/haswell/libopencv_videostab.so.3.3.1
/usr/lib64/libopencv_calib3d.so.3.3
/usr/lib64/libopencv_calib3d.so.3.3.1
/usr/lib64/libopencv_core.so.3.3
/usr/lib64/libopencv_core.so.3.3.1
/usr/lib64/libopencv_dnn.so.3.3
/usr/lib64/libopencv_dnn.so.3.3.1
/usr/lib64/libopencv_features2d.so.3.3
/usr/lib64/libopencv_features2d.so.3.3.1
/usr/lib64/libopencv_flann.so.3.3
/usr/lib64/libopencv_flann.so.3.3.1
/usr/lib64/libopencv_highgui.so.3.3
/usr/lib64/libopencv_highgui.so.3.3.1
/usr/lib64/libopencv_imgcodecs.so.3.3
/usr/lib64/libopencv_imgcodecs.so.3.3.1
/usr/lib64/libopencv_imgproc.so.3.3
/usr/lib64/libopencv_imgproc.so.3.3.1
/usr/lib64/libopencv_ml.so.3.3
/usr/lib64/libopencv_ml.so.3.3.1
/usr/lib64/libopencv_objdetect.so.3.3
/usr/lib64/libopencv_objdetect.so.3.3.1
/usr/lib64/libopencv_photo.so.3.3
/usr/lib64/libopencv_photo.so.3.3.1
/usr/lib64/libopencv_shape.so.3.3
/usr/lib64/libopencv_shape.so.3.3.1
/usr/lib64/libopencv_stitching.so.3.3
/usr/lib64/libopencv_stitching.so.3.3.1
/usr/lib64/libopencv_superres.so.3.3
/usr/lib64/libopencv_superres.so.3.3.1
/usr/lib64/libopencv_video.so.3.3
/usr/lib64/libopencv_video.so.3.3.1
/usr/lib64/libopencv_videoio.so.3.3
/usr/lib64/libopencv_videoio.so.3.3.1
/usr/lib64/libopencv_videostab.so.3.3
/usr/lib64/libopencv_videostab.so.3.3.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-opencv-soname33/3rdparty_cpufeatures_LICENSE
/usr/share/package-licenses/compat-opencv-soname33/3rdparty_ffmpeg_license.txt
/usr/share/package-licenses/compat-opencv-soname33/3rdparty_ittnotify_src_ittnotify_LICENSE.BSD
/usr/share/package-licenses/compat-opencv-soname33/3rdparty_ittnotify_src_ittnotify_LICENSE.GPL
/usr/share/package-licenses/compat-opencv-soname33/3rdparty_libjasper_LICENSE
/usr/share/package-licenses/compat-opencv-soname33/3rdparty_libjasper_copyright
/usr/share/package-licenses/compat-opencv-soname33/3rdparty_libpng_LICENSE
/usr/share/package-licenses/compat-opencv-soname33/3rdparty_libtiff_COPYRIGHT
/usr/share/package-licenses/compat-opencv-soname33/3rdparty_openexr_LICENSE
/usr/share/package-licenses/compat-opencv-soname33/3rdparty_protobuf_LICENSE
/usr/share/package-licenses/compat-opencv-soname33/LICENSE
/usr/share/package-licenses/compat-opencv-soname33/modules_dnn_src_torch_COPYRIGHT.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
