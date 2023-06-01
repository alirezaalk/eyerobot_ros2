// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_interface:msg/RobotPose.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__STRUCT_HPP_
#define ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'coordinate'
#include "geometry_msgs/msg/detail/pose__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__robot_interface__msg__RobotPose __attribute__((deprecated))
#else
# define DEPRECATED__robot_interface__msg__RobotPose __declspec(deprecated)
#endif

namespace robot_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RobotPose_
{
  using Type = RobotPose_<ContainerAllocator>;

  explicit RobotPose_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : coordinate(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->name = "";
      this->en0 = 0.0f;
      this->en1 = 0.0f;
      this->en2 = 0.0f;
      this->en3 = 0.0f;
      this->en4 = 0.0f;
      this->mode = 0.0f;
      this->speed = 0ull;
      this->command = 0.0f;
    }
  }

  explicit RobotPose_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : name(_alloc),
    coordinate(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->name = "";
      this->en0 = 0.0f;
      this->en1 = 0.0f;
      this->en2 = 0.0f;
      this->en3 = 0.0f;
      this->en4 = 0.0f;
      this->mode = 0.0f;
      this->speed = 0ull;
      this->command = 0.0f;
    }
  }

  // field types and members
  using _name_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _name_type name;
  using _en0_type =
    float;
  _en0_type en0;
  using _en1_type =
    float;
  _en1_type en1;
  using _en2_type =
    float;
  _en2_type en2;
  using _en3_type =
    float;
  _en3_type en3;
  using _en4_type =
    float;
  _en4_type en4;
  using _coordinate_type =
    geometry_msgs::msg::Pose_<ContainerAllocator>;
  _coordinate_type coordinate;
  using _mode_type =
    float;
  _mode_type mode;
  using _speed_type =
    uint64_t;
  _speed_type speed;
  using _command_type =
    float;
  _command_type command;

  // setters for named parameter idiom
  Type & set__name(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->name = _arg;
    return *this;
  }
  Type & set__en0(
    const float & _arg)
  {
    this->en0 = _arg;
    return *this;
  }
  Type & set__en1(
    const float & _arg)
  {
    this->en1 = _arg;
    return *this;
  }
  Type & set__en2(
    const float & _arg)
  {
    this->en2 = _arg;
    return *this;
  }
  Type & set__en3(
    const float & _arg)
  {
    this->en3 = _arg;
    return *this;
  }
  Type & set__en4(
    const float & _arg)
  {
    this->en4 = _arg;
    return *this;
  }
  Type & set__coordinate(
    const geometry_msgs::msg::Pose_<ContainerAllocator> & _arg)
  {
    this->coordinate = _arg;
    return *this;
  }
  Type & set__mode(
    const float & _arg)
  {
    this->mode = _arg;
    return *this;
  }
  Type & set__speed(
    const uint64_t & _arg)
  {
    this->speed = _arg;
    return *this;
  }
  Type & set__command(
    const float & _arg)
  {
    this->command = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_interface::msg::RobotPose_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_interface::msg::RobotPose_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_interface::msg::RobotPose_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_interface::msg::RobotPose_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_interface::msg::RobotPose_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_interface::msg::RobotPose_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_interface::msg::RobotPose_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_interface::msg::RobotPose_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_interface::msg::RobotPose_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_interface::msg::RobotPose_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_interface__msg__RobotPose
    std::shared_ptr<robot_interface::msg::RobotPose_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_interface__msg__RobotPose
    std::shared_ptr<robot_interface::msg::RobotPose_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotPose_ & other) const
  {
    if (this->name != other.name) {
      return false;
    }
    if (this->en0 != other.en0) {
      return false;
    }
    if (this->en1 != other.en1) {
      return false;
    }
    if (this->en2 != other.en2) {
      return false;
    }
    if (this->en3 != other.en3) {
      return false;
    }
    if (this->en4 != other.en4) {
      return false;
    }
    if (this->coordinate != other.coordinate) {
      return false;
    }
    if (this->mode != other.mode) {
      return false;
    }
    if (this->speed != other.speed) {
      return false;
    }
    if (this->command != other.command) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotPose_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotPose_

// alias to use template instance with default allocator
using RobotPose =
  robot_interface::msg::RobotPose_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace robot_interface

#endif  // ROBOT_INTERFACE__MSG__DETAIL__ROBOT_POSE__STRUCT_HPP_
