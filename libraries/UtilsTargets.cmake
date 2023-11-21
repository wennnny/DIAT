# Generated by CMake

if("${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}" LESS 2.8)
   message(FATAL_ERROR "CMake >= 2.8.0 required")
endif()
if(CMAKE_VERSION VERSION_LESS "2.8.3")
   message(FATAL_ERROR "CMake >= 2.8.3 required")
endif()
cmake_policy(PUSH)
cmake_policy(VERSION 2.8.3...3.23)
#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Protect against multiple inclusion, which would fail when already imported targets are added once more.
set(_cmake_targets_defined "")
set(_cmake_targets_not_defined "")
set(_cmake_expected_targets "")
foreach(_cmake_expected_target IN ITEMS utils::RealTime utils::VirtualTime utils::Time utils::Console utils::Param utils::InitTIMTool utils::PluginLoader)
  list(APPEND _cmake_expected_targets "${_cmake_expected_target}")
  if(TARGET "${_cmake_expected_target}")
    list(APPEND _cmake_targets_defined "${_cmake_expected_target}")
  else()
    list(APPEND _cmake_targets_not_defined "${_cmake_expected_target}")
  endif()
endforeach()
unset(_cmake_expected_target)
if(_cmake_targets_defined STREQUAL _cmake_expected_targets)
  unset(_cmake_targets_defined)
  unset(_cmake_targets_not_defined)
  unset(_cmake_expected_targets)
  unset(CMAKE_IMPORT_FILE_VERSION)
  cmake_policy(POP)
  return()
endif()
if(NOT _cmake_targets_defined STREQUAL "")
  string(REPLACE ";" ", " _cmake_targets_defined_text "${_cmake_targets_defined}")
  string(REPLACE ";" ", " _cmake_targets_not_defined_text "${_cmake_targets_not_defined}")
  message(FATAL_ERROR "Some (but not all) targets in this export set were already defined.\nTargets Defined: ${_cmake_targets_defined_text}\nTargets not yet defined: ${_cmake_targets_not_defined_text}\n")
endif()
unset(_cmake_targets_defined)
unset(_cmake_targets_not_defined)
unset(_cmake_expected_targets)


# Create imported target utils::RealTime
add_library(utils::RealTime STATIC IMPORTED)

set_target_properties(utils::RealTime PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "D:/7_Pick_And_Place_Machine/pnp_1_1_0/src/utils/include"
  INTERFACE_LINK_LIBRARIES "C:/msys64/mingw64/lib/libboost_date_time-mt.dll.a;C:/msys64/mingw64/lib/libboost_thread-mt.dll.a;C:/msys64/mingw64/lib/libboost_math_c99-mt.dll.a;C:/msys64/mingw64/lib/libboost_chrono-mt.dll.a;C:/msys64/mingw64/lib/libboost_atomic-mt.dll.a"
)

# Create imported target utils::VirtualTime
add_library(utils::VirtualTime STATIC IMPORTED)

set_target_properties(utils::VirtualTime PROPERTIES
  INTERFACE_LINK_LIBRARIES "C:/msys64/mingw64/lib/libboost_date_time-mt.dll.a;C:/msys64/mingw64/lib/libboost_thread-mt.dll.a;C:/msys64/mingw64/lib/libboost_math_c99-mt.dll.a;C:/msys64/mingw64/lib/libboost_chrono-mt.dll.a;C:/msys64/mingw64/lib/libboost_atomic-mt.dll.a;D:/7_Pick_And_Place_Machine/pnp_1_1_0/src/utils/../DIATwin/lib/controller/Controller.dll;D:/7_Pick_And_Place_Machine/pnp_1_1_0/src/utils/../DIATwin/lib/controller/CppController.dll;D:/7_Pick_And_Place_Machine/pnp_1_1_0/src/../bin/libVDDManager.dll"
)

# Create imported target utils::Time
add_library(utils::Time STATIC IMPORTED)

set_target_properties(utils::Time PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "D:/7_Pick_And_Place_Machine/pnp_1_1_0/src/utils/include"
  INTERFACE_LINK_LIBRARIES "utils::RealTime;utils::VirtualTime"
)

# Create imported target utils::Console
add_library(utils::Console STATIC IMPORTED)

set_target_properties(utils::Console PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "D:/7_Pick_And_Place_Machine/pnp_1_1_0/src/utils/include"
  INTERFACE_LINK_LIBRARIES "C:/msys64/mingw64/lib/libboost_date_time-mt.dll.a;C:/msys64/mingw64/lib/libboost_thread-mt.dll.a;C:/msys64/mingw64/lib/libboost_math_c99-mt.dll.a;C:/msys64/mingw64/lib/libboost_chrono-mt.dll.a;C:/msys64/mingw64/lib/libboost_atomic-mt.dll.a;utils::Time"
)

# Create imported target utils::Param
add_library(utils::Param STATIC IMPORTED)

set_target_properties(utils::Param PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "D:/7_Pick_And_Place_Machine/pnp_1_1_0/src/utils/include;D:/7_Pick_And_Place_Machine/pnp_1_1_0/src/utils/third_party/rapidjson/include"
  INTERFACE_LINK_LIBRARIES "utils::Console"
)

# Create imported target utils::InitTIMTool
add_library(utils::InitTIMTool STATIC IMPORTED)

set_target_properties(utils::InitTIMTool PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "D:/7_Pick_And_Place_Machine/pnp_1_1_0/src/utils/include"
  INTERFACE_LINK_LIBRARIES "utils::Param"
)

# Create imported target utils::PluginLoader
add_library(utils::PluginLoader STATIC IMPORTED)

set_target_properties(utils::PluginLoader PROPERTIES
  INTERFACE_INCLUDE_DIRECTORIES "D:/7_Pick_And_Place_Machine/pnp_1_1_0/src/utils/include"
  INTERFACE_LINK_LIBRARIES "utils::Param"
)

# Import target "utils::RealTime" for configuration "Debug"
set_property(TARGET utils::RealTime APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(utils::RealTime PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "D:/7_Pick_And_Place_Machine/pnp_1_1_0/lib/libRealTime.a"
  )

# Import target "utils::VirtualTime" for configuration "Debug"
set_property(TARGET utils::VirtualTime APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(utils::VirtualTime PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "D:/7_Pick_And_Place_Machine/pnp_1_1_0/lib/libVirtualTime.a"
  )

# Import target "utils::Time" for configuration "Debug"
set_property(TARGET utils::Time APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(utils::Time PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "D:/7_Pick_And_Place_Machine/pnp_1_1_0/lib/libTime.a"
  )

# Import target "utils::Console" for configuration "Debug"
set_property(TARGET utils::Console APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(utils::Console PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "D:/7_Pick_And_Place_Machine/pnp_1_1_0/lib/libConsole.a"
  )

# Import target "utils::Param" for configuration "Debug"
set_property(TARGET utils::Param APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(utils::Param PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "D:/7_Pick_And_Place_Machine/pnp_1_1_0/lib/libParam.a"
  )

# Import target "utils::InitTIMTool" for configuration "Debug"
set_property(TARGET utils::InitTIMTool APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(utils::InitTIMTool PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "D:/7_Pick_And_Place_Machine/pnp_1_1_0/lib/libInitTIMTool.a"
  )

# Import target "utils::PluginLoader" for configuration "Debug"
set_property(TARGET utils::PluginLoader APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(utils::PluginLoader PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_DEBUG "CXX"
  IMPORTED_LOCATION_DEBUG "D:/7_Pick_And_Place_Machine/pnp_1_1_0/lib/libPluginLoader.a"
  )

# This file does not depend on other imported targets which have
# been exported from the same project but in a separate export set.

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
cmake_policy(POP)