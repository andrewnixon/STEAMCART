cmake_minimum_required (VERSION 2.8)
project (STEAMCART)

# The version number.
set (STEAMCART_VERSION_MAJOR 0)
set (STEAMCART_VERSION_MINOR 1)

set(CMAKE_CXX_STANDARD 14)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/SteamcartConfig.h.in"
  "${PROJECT_BINARY_DIR}/SteamcartConfig.h"
)

SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

include_directories(
  ${PROJECT_SOURCE_DIR}/source/general/include/
)

#=========================================================
# Locate sources and headers for this project
FILE(GLOB sources
  ${PROJECT_SOURCE_DIR}/source/general/src/*.cxx
)

FILE(GLOB headers
  ${PROJECT_SOURCE_DIR}/source/general/include/*.h
)

# add the executable
add_executable(steamcart steamcart.cxx ${sources} ${headers})
