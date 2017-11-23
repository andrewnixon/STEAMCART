cmake_minimum_required (VERSION 2.6)
project (STEAMCART)
# The version number.
set (STEAMCART_VERSION_MAJOR 0)
set (STEAMCART_VERSION_MINOR 1)

# configure a header file to pass some of the CMake settings
# to the source code
configure_file (
  "${PROJECT_SOURCE_DIR}/SteamcartConfig.h.in"
  "${PROJECT_BINARY_DIR}/SteamcartConfig.h"
  )

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

# add the executable
add_executable(steamcart steamcart.cxx)
