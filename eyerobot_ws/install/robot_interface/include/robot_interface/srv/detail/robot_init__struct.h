// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_interface:srv/RobotInit.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__STRUCT_H_
#define ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in srv/RobotInit in the package robot_interface.
typedef struct robot_interface__srv__RobotInit_Request
{
  int16_t command;
} robot_interface__srv__RobotInit_Request;

// Struct for a sequence of robot_interface__srv__RobotInit_Request.
typedef struct robot_interface__srv__RobotInit_Request__Sequence
{
  robot_interface__srv__RobotInit_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interface__srv__RobotInit_Request__Sequence;


// Constants defined in the message

// Struct defined in srv/RobotInit in the package robot_interface.
typedef struct robot_interface__srv__RobotInit_Response
{
  bool sucess;
} robot_interface__srv__RobotInit_Response;

// Struct for a sequence of robot_interface__srv__RobotInit_Response.
typedef struct robot_interface__srv__RobotInit_Response__Sequence
{
  robot_interface__srv__RobotInit_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interface__srv__RobotInit_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__STRUCT_H_
