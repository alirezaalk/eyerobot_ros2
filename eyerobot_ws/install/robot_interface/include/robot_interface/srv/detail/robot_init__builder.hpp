// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interface:srv/RobotInit.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__BUILDER_HPP_
#define ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__BUILDER_HPP_

#include "robot_interface/srv/detail/robot_init__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_interface
{

namespace srv
{

namespace builder
{

class Init_RobotInit_Request_command
{
public:
  Init_RobotInit_Request_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interface::srv::RobotInit_Request command(::robot_interface::srv::RobotInit_Request::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interface::srv::RobotInit_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interface::srv::RobotInit_Request>()
{
  return robot_interface::srv::builder::Init_RobotInit_Request_command();
}

}  // namespace robot_interface


namespace robot_interface
{

namespace srv
{

namespace builder
{

class Init_RobotInit_Response_sucess
{
public:
  Init_RobotInit_Response_sucess()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interface::srv::RobotInit_Response sucess(::robot_interface::srv::RobotInit_Response::_sucess_type arg)
  {
    msg_.sucess = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interface::srv::RobotInit_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interface::srv::RobotInit_Response>()
{
  return robot_interface::srv::builder::Init_RobotInit_Response_sucess();
}

}  // namespace robot_interface

#endif  // ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__BUILDER_HPP_
