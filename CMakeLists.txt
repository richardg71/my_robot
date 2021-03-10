cmake_minimum_required(VERSION 2.8.3)
project(my_robot)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)

## Declare ROS messages and services
#add_message_files(FILES Num.msg)
#add_service_files(FILES AddTwoInts.srv)

## Generate added messages and services
#generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS} /usr/local/include/sphinxbase /usr/local/include/pocketsphinx)

add_executable(main_subscriber src/main_subscriber.cpp)
target_link_libraries(main_subscriber ${catkin_LIBRARIES})
add_dependencies(main_subscriber my_robot_generate_messages_cpp)

add_executable(continuous src/continuous.cpp)
target_link_libraries(continuous
  ${catkin_LIBRARIES}
  pocketsphinx
  sphinxbase
  sphinxad
  )
add_dependencies(continuous my_robot_generate_messages_cpp)

catkin_install_python(PROGRAMS
  scripts/servo.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  )
