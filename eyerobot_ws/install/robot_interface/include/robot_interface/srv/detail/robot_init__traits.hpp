// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_interface:srv/RobotInit.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__TRAITS_HPP_
#define ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__TRAITS_HPP_

#include "robot_interface/srv/detail/robot_init__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_interface::srv::RobotInit_Request>()
{
  return "robot_interface::srv::RobotInit_Request";
}

template<>
inline const char * name<robot_interface::srv::RobotInit_Request>()
{
  return "robot_interface/srv/RobotInit_Request";
}

template<>
struct has_fixed_size<robot_interface::srv::RobotInit_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_interface::srv::RobotInit_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_interface::srv::RobotInit_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_interface::srv::RobotInit_Response>()
{
  return "robot_interface::srv::RobotInit_Response";
}

template<>
inline const char * name<robot_interface::srv::RobotInit_Response>()
{
  return "robot_interface/srv/RobotInit_Response";
}

template<>
struct has_fixed_size<robot_interface::srv::RobotInit_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_interface::srv::RobotInit_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_interface::srv::RobotInit_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_interface::srv::RobotInit>()
{
  return "robot_interface::srv::RobotInit";
}

template<>
inline const char * name<robot_interface::srv::RobotInit>()
{
  return "robot_interface/srv/RobotInit";
}

template<>
struct has_fixed_size<robot_interface::srv::RobotInit>
  : std::integral_constant<
    bool,
    has_fixed_size<robot_interface::srv::RobotInit_Request>::value &&
    has_fixed_size<robot_interface::srv::RobotInit_Response>::value
  >
{
};

template<>
struct has_bounded_size<robot_interface::srv::RobotInit>
  : std::integral_constant<
    bool,
    has_bounded_size<robot_interface::srv::RobotInit_Request>::value &&
    has_bounded_size<robot_interface::srv::RobotInit_Response>::value
  >
{
};

template<>
struct is_service<robot_interface::srv::RobotInit>
  : std::true_type
{
};

template<>
struct is_service_request<robot_interface::srv::RobotInit_Request>
  : std::true_type
{
};

template<>
struct is_service_response<robot_interface::srv::RobotInit_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__TRAITS_HPP_
