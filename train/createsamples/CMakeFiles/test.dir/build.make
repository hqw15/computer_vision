# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.14

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CMake.app/Contents/bin/cmake

# The command to remove a file.
RM = /Applications/CMake.app/Contents/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/hqw/Desktop/objectDetect/train/createsamples

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/hqw/Desktop/objectDetect/train/createsamples

# Include any dependencies generated for this target.
include CMakeFiles/test.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/test.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test.dir/flags.make

CMakeFiles/test.dir/createsamples.o: CMakeFiles/test.dir/flags.make
CMakeFiles/test.dir/createsamples.o: createsamples.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/hqw/Desktop/objectDetect/train/createsamples/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/test.dir/createsamples.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test.dir/createsamples.o -c /Users/hqw/Desktop/objectDetect/train/createsamples/createsamples.cpp

CMakeFiles/test.dir/createsamples.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test.dir/createsamples.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/hqw/Desktop/objectDetect/train/createsamples/createsamples.cpp > CMakeFiles/test.dir/createsamples.i

CMakeFiles/test.dir/createsamples.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test.dir/createsamples.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/hqw/Desktop/objectDetect/train/createsamples/createsamples.cpp -o CMakeFiles/test.dir/createsamples.s

CMakeFiles/test.dir/utility.o: CMakeFiles/test.dir/flags.make
CMakeFiles/test.dir/utility.o: utility.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/hqw/Desktop/objectDetect/train/createsamples/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/test.dir/utility.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test.dir/utility.o -c /Users/hqw/Desktop/objectDetect/train/createsamples/utility.cpp

CMakeFiles/test.dir/utility.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test.dir/utility.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/hqw/Desktop/objectDetect/train/createsamples/utility.cpp > CMakeFiles/test.dir/utility.i

CMakeFiles/test.dir/utility.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test.dir/utility.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/hqw/Desktop/objectDetect/train/createsamples/utility.cpp -o CMakeFiles/test.dir/utility.s

# Object files for target test
test_OBJECTS = \
"CMakeFiles/test.dir/createsamples.o" \
"CMakeFiles/test.dir/utility.o"

# External object files for target test
test_EXTERNAL_OBJECTS =

test: CMakeFiles/test.dir/createsamples.o
test: CMakeFiles/test.dir/utility.o
test: CMakeFiles/test.dir/build.make
test: /usr/local/lib/libopencv_gapi.4.0.1.dylib
test: /usr/local/lib/libopencv_stitching.4.0.1.dylib
test: /usr/local/lib/libopencv_aruco.4.0.1.dylib
test: /usr/local/lib/libopencv_bgsegm.4.0.1.dylib
test: /usr/local/lib/libopencv_bioinspired.4.0.1.dylib
test: /usr/local/lib/libopencv_ccalib.4.0.1.dylib
test: /usr/local/lib/libopencv_dnn_objdetect.4.0.1.dylib
test: /usr/local/lib/libopencv_dpm.4.0.1.dylib
test: /usr/local/lib/libopencv_face.4.0.1.dylib
test: /usr/local/lib/libopencv_fuzzy.4.0.1.dylib
test: /usr/local/lib/libopencv_hfs.4.0.1.dylib
test: /usr/local/lib/libopencv_img_hash.4.0.1.dylib
test: /usr/local/lib/libopencv_line_descriptor.4.0.1.dylib
test: /usr/local/lib/libopencv_reg.4.0.1.dylib
test: /usr/local/lib/libopencv_rgbd.4.0.1.dylib
test: /usr/local/lib/libopencv_saliency.4.0.1.dylib
test: /usr/local/lib/libopencv_stereo.4.0.1.dylib
test: /usr/local/lib/libopencv_structured_light.4.0.1.dylib
test: /usr/local/lib/libopencv_superres.4.0.1.dylib
test: /usr/local/lib/libopencv_surface_matching.4.0.1.dylib
test: /usr/local/lib/libopencv_tracking.4.0.1.dylib
test: /usr/local/lib/libopencv_videostab.4.0.1.dylib
test: /usr/local/lib/libopencv_xfeatures2d.4.0.1.dylib
test: /usr/local/lib/libopencv_xobjdetect.4.0.1.dylib
test: /usr/local/lib/libopencv_xphoto.4.0.1.dylib
test: /usr/local/lib/libopencv_shape.4.0.1.dylib
test: /usr/local/lib/libopencv_phase_unwrapping.4.0.1.dylib
test: /usr/local/lib/libopencv_optflow.4.0.1.dylib
test: /usr/local/lib/libopencv_ximgproc.4.0.1.dylib
test: /usr/local/lib/libopencv_dnn.4.0.1.dylib
test: /usr/local/lib/libopencv_datasets.4.0.1.dylib
test: /usr/local/lib/libopencv_ml.4.0.1.dylib
test: /usr/local/lib/libopencv_plot.4.0.1.dylib
test: /usr/local/lib/libopencv_video.4.0.1.dylib
test: /usr/local/lib/libopencv_objdetect.4.0.1.dylib
test: /usr/local/lib/libopencv_calib3d.4.0.1.dylib
test: /usr/local/lib/libopencv_features2d.4.0.1.dylib
test: /usr/local/lib/libopencv_flann.4.0.1.dylib
test: /usr/local/lib/libopencv_highgui.4.0.1.dylib
test: /usr/local/lib/libopencv_videoio.4.0.1.dylib
test: /usr/local/lib/libopencv_imgcodecs.4.0.1.dylib
test: /usr/local/lib/libopencv_photo.4.0.1.dylib
test: /usr/local/lib/libopencv_imgproc.4.0.1.dylib
test: /usr/local/lib/libopencv_core.4.0.1.dylib
test: CMakeFiles/test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/hqw/Desktop/objectDetect/train/createsamples/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable test"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test.dir/build: test

.PHONY : CMakeFiles/test.dir/build

CMakeFiles/test.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test.dir/clean

CMakeFiles/test.dir/depend:
	cd /Users/hqw/Desktop/objectDetect/train/createsamples && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/hqw/Desktop/objectDetect/train/createsamples /Users/hqw/Desktop/objectDetect/train/createsamples /Users/hqw/Desktop/objectDetect/train/createsamples /Users/hqw/Desktop/objectDetect/train/createsamples /Users/hqw/Desktop/objectDetect/train/createsamples/CMakeFiles/test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test.dir/depend
