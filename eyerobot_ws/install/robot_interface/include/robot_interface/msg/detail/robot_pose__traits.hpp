// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_interface:msg/RobotPose.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__TRAITS_HPP_
#define ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__TRAITS_HPP_

#include "robot_interface/msg/detail/robot_pose__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'coordinate'
#include "geometry_msgs/msg/detail/pose__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_interface::msg::RobotPose>()
{
  return "robot_interface::msg::RobotPose";
}

template<>
inline const char * name<robot_interface::msg::RobotPose>()
{
  return "robot_interface/msg/RobotPose";
}

template<>
struct has_fixed_size<robot_interface::msg::RobotPose>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<robot_interface::msg::RobotPose>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<robot_interface::msg::RobotPose>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__TRAITS_HPP_
