// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from robot_interface:msg/RobotPose.idl
// generated code does not contain a copyright notice
#include "robot_interface/msg/detail/robot_pose__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `name`
#include "rosidl_runtime_c/string_functions.h"
// Member `coordinate`
#include "geometry_msgs/msg/detail/pose__functions.h"

bool
robot_interface__msg__RobotPose__init(robot_interface__msg__RobotPose * msg)
{
  if (!msg) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__init(&msg->name)) {
    robot_interface__msg__RobotPose__fini(msg);
    return false;
  }
  // en0
  // en1
  // en2
  // en3
  // en4
  // coordinate
  if (!geometry_msgs__msg__Pose__init(&msg->coordinate)) {
    robot_interface__msg__RobotPose__fini(msg);
    return false;
  }
  // mode
  // speed
  // command
  return true;
}

void
robot_interface__msg__RobotPose__fini(robot_interface__msg__RobotPose * msg)
{
  if (!msg) {
    return;
  }
  // name
  rosidl_runtime_c__String__fini(&msg->name);
  // en0
  // en1
  // en2
  // en3
  // en4
  // coordinate
  geometry_msgs__msg__Pose__fini(&msg->coordinate);
  // mode
  // speed
  // command
}

bool
robot_interface__msg__RobotPose__are_equal(const robot_interface__msg__RobotPose * lhs, const robot_interface__msg__RobotPose * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->name), &(rhs->name)))
  {
    return false;
  }
  // en0
  if (lhs->en0 != rhs->en0) {
    return false;
  }
  // en1
  if (lhs->en1 != rhs->en1) {
    return false;
  }
  // en2
  if (lhs->en2 != rhs->en2) {
    return false;
  }
  // en3
  if (lhs->en3 != rhs->en3) {
    return false;
  }
  // en4
  if (lhs->en4 != rhs->en4) {
    return false;
  }
  // coordinate
  if (!geometry_msgs__msg__Pose__are_equal(
      &(lhs->coordinate), &(rhs->coordinate)))
  {
    return false;
  }
  // mode
  if (lhs->mode != rhs->mode) {
    return false;
  }
  // speed
  if (lhs->speed != rhs->speed) {
    return false;
  }
  // command
  if (lhs->command != rhs->command) {
    return false;
  }
  return true;
}

bool
robot_interface__msg__RobotPose__copy(
  const robot_interface__msg__RobotPose * input,
  robot_interface__msg__RobotPose * output)
{
  if (!input || !output) {
    return false;
  }
  // name
  if (!rosidl_runtime_c__String__copy(
      &(input->name), &(output->name)))
  {
    return false;
  }
  // en0
  output->en0 = input->en0;
  // en1
  output->en1 = input->en1;
  // en2
  output->en2 = input->en2;
  // en3
  output->en3 = input->en3;
  // en4
  output->en4 = input->en4;
  // coordinate
  if (!geometry_msgs__msg__Pose__copy(
      &(input->coordinate), &(output->coordinate)))
  {
    return false;
  }
  // mode
  output->mode = input->mode;
  // speed
  output->speed = input->speed;
  // command
  output->command = input->command;
  return true;
}

robot_interface__msg__RobotPose *
robot_interface__msg__RobotPose__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_interface__msg__RobotPose * msg = (robot_interface__msg__RobotPose *)allocator.allocate(sizeof(robot_interface__msg__RobotPose), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(robot_interface__msg__RobotPose));
  bool success = robot_interface__msg__RobotPose__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
robot_interface__msg__RobotPose__destroy(robot_interface__msg__RobotPose * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    robot_interface__msg__RobotPose__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
robot_interface__msg__RobotPose__Sequence__init(robot_interface__msg__RobotPose__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_interface__msg__RobotPose * data = NULL;

  if (size) {
    data = (robot_interface__msg__RobotPose *)allocator.zero_allocate(size, sizeof(robot_interface__msg__RobotPose), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = robot_interface__msg__RobotPose__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        robot_interface__msg__RobotPose__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
robot_interface__msg__RobotPose__Sequence__fini(robot_interface__msg__RobotPose__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      robot_interface__msg__RobotPose__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

robot_interface__msg__RobotPose__Sequence *
robot_interface__msg__RobotPose__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  robot_interface__msg__RobotPose__Sequence * array = (robot_interface__msg__RobotPose__Sequence *)allocator.allocate(sizeof(robot_interface__msg__RobotPose__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = robot_interface__msg__RobotPose__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
robot_interface__msg__RobotPose__Sequence__destroy(robot_interface__msg__RobotPose__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    robot_interface__msg__RobotPose__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
robot_interface__msg__RobotPose__Sequence__are_equal(const robot_interface__msg__RobotPose__Sequence * lhs, const robot_interface__msg__RobotPose__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!robot_interface__msg__RobotPose__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
robot_interface__msg__RobotPose__Sequence__copy(
  const robot_interface__msg__RobotPose__Sequence * input,
  robot_interface__msg__RobotPose__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(robot_interface__msg__RobotPose);
    robot_interface__msg__RobotPose * data =
      (robot_interface__msg__RobotPose *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!robot_interface__msg__RobotPose__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          robot_interface__msg__RobotPose__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!robot_interface__msg__RobotPose__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
