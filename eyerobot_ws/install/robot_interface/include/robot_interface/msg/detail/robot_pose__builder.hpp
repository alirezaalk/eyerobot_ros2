// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interface:msg/RobotPose.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__BUILDER_HPP_
#define ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__BUILDER_HPP_

#include "robot_interface/msg/detail/robot_pose__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace robot_interface
{

namespace msg
{

namespace builder
{

class Init_RobotPose_command
{
public:
  explicit Init_RobotPose_command(::robot_interface::msg::RobotPose & msg)
  : msg_(msg)
  {}
  ::robot_interface::msg::RobotPose command(::robot_interface::msg::RobotPose::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interface::msg::RobotPose msg_;
};

class Init_RobotPose_speed
{
public:
  explicit Init_RobotPose_speed(::robot_interface::msg::RobotPose & msg)
  : msg_(msg)
  {}
  Init_RobotPose_command speed(::robot_interface::msg::RobotPose::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return Init_RobotPose_command(msg_);
  }

private:
  ::robot_interface::msg::RobotPose msg_;
};

class Init_RobotPose_mode
{
public:
  explicit Init_RobotPose_mode(::robot_interface::msg::RobotPose & msg)
  : msg_(msg)
  {}
  Init_RobotPose_speed mode(::robot_interface::msg::RobotPose::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return Init_RobotPose_speed(msg_);
  }

private:
  ::robot_interface::msg::RobotPose msg_;
};

class Init_RobotPose_coordinate
{
public:
  explicit Init_RobotPose_coordinate(::robot_interface::msg::RobotPose & msg)
  : msg_(msg)
  {}
  Init_RobotPose_mode coordinate(::robot_interface::msg::RobotPose::_coordinate_type arg)
  {
    msg_.coordinate = std::move(arg);
    return Init_RobotPose_mode(msg_);
  }

private:
  ::robot_interface::msg::RobotPose msg_;
};

class Init_RobotPose_en4
{
public:
  explicit Init_RobotPose_en4(::robot_interface::msg::RobotPose & msg)
  : msg_(msg)
  {}
  Init_RobotPose_coordinate en4(::robot_interface::msg::RobotPose::_en4_type arg)
  {
    msg_.en4 = std::move(arg);
    return Init_RobotPose_coordinate(msg_);
  }

private:
  ::robot_interface::msg::RobotPose msg_;
};

class Init_RobotPose_en3
{
public:
  explicit Init_RobotPose_en3(::robot_interface::msg::RobotPose & msg)
  : msg_(msg)
  {}
  Init_RobotPose_en4 en3(::robot_interface::msg::RobotPose::_en3_type arg)
  {
    msg_.en3 = std::move(arg);
    return Init_RobotPose_en4(msg_);
  }

private:
  ::robot_interface::msg::RobotPose msg_;
};

class Init_RobotPose_en2
{
public:
  explicit Init_RobotPose_en2(::robot_interface::msg::RobotPose & msg)
  : msg_(msg)
  {}
  Init_RobotPose_en3 en2(::robot_interface::msg::RobotPose::_en2_type arg)
  {
    msg_.en2 = std::move(arg);
    return Init_RobotPose_en3(msg_);
  }

private:
  ::robot_interface::msg::RobotPose msg_;
};

class Init_RobotPose_en1
{
public:
  explicit Init_RobotPose_en1(::robot_interface::msg::RobotPose & msg)
  : msg_(msg)
  {}
  Init_RobotPose_en2 en1(::robot_interface::msg::RobotPose::_en1_type arg)
  {
    msg_.en1 = std::move(arg);
    return Init_RobotPose_en2(msg_);
  }

private:
  ::robot_interface::msg::RobotPose msg_;
};

class Init_RobotPose_en0
{
public:
  explicit Init_RobotPose_en0(::robot_interface::msg::RobotPose & msg)
  : msg_(msg)
  {}
  Init_RobotPose_en1 en0(::robot_interface::msg::RobotPose::_en0_type arg)
  {
    msg_.en0 = std::move(arg);
    return Init_RobotPose_en1(msg_);
  }

private:
  ::robot_interface::msg::RobotPose msg_;
};

class Init_RobotPose_name
{
public:
  Init_RobotPose_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotPose_en0 name(::robot_interface::msg::RobotPose::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_RobotPose_en0(msg_);
  }

private:
  ::robot_interface::msg::RobotPose msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interface::msg::RobotPose>()
{
  return robot_interface::msg::builder::Init_RobotPose_name();
}

}  // namespace robot_interface

#endif  // ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__BUILDER_HPP_
