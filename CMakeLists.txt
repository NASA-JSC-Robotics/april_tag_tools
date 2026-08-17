cmake_minimum_required(VERSION 3.5)
project(april_tag_tools)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY 36h11
  DESTINATION share/${PROJECT_NAME}
)

ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})

ament_package()
