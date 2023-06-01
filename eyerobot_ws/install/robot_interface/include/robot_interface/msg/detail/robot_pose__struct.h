// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_interface:msg/RobotPose.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__STRUCT_H_
#define ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'name'
#include "rosidl_runtime_c/string.h"
// Member 'coordinate'
#include "geometry_msgs/msg/detail/pose__struct.h"

// Struct defined in msg/RobotPose in the package robot_interface.
typedef struct robot_interface__msg__RobotPose
{
  rosidl_runtime_c__String name;
  float en0;
  float en1;
  float en2;
  float en3;
  float en4;
  geometry_msgs__msg__Pose coordinate;
  float mode;
  uint64_t speed;
  float command;
} robot_interface__msg__RobotPose;

// Struct for a sequence of robot_interface__msg__RobotPose.
typedef struct robot_interface__msg__RobotPose__Sequence
{
  robot_interface__msg__RobotPose * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interface__msg__RobotPose__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__STRUCT_H_
