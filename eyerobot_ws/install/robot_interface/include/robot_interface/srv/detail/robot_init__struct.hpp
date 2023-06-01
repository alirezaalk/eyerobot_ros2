// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robot_interface:srv/RobotInit.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__STRUCT_HPP_
#define ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__robot_interface__srv__RobotInit_Request __attribute__((deprecated))
#else
# define DEPRECATED__robot_interface__srv__RobotInit_Request __declspec(deprecated)
#endif

namespace robot_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct RobotInit_Request_
{
  using Type = RobotInit_Request_<ContainerAllocator>;

  explicit RobotInit_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command = 0;
    }
  }

  explicit RobotInit_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command = 0;
    }
  }

  // field types and members
  using _command_type =
    int16_t;
  _command_type command;

  // setters for named parameter idiom
  Type & set__command(
    const int16_t & _arg)
  {
    this->command = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_interface::srv::RobotInit_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_interface::srv::RobotInit_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_interface::srv::RobotInit_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_interface::srv::RobotInit_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_interface::srv::RobotInit_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_interface::srv::RobotInit_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_interface::srv::RobotInit_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_interface::srv::RobotInit_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_interface::srv::RobotInit_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_interface::srv::RobotInit_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_interface__srv__RobotInit_Request
    std::shared_ptr<robot_interface::srv::RobotInit_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_interface__srv__RobotInit_Request
    std::shared_ptr<robot_interface::srv::RobotInit_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotInit_Request_ & other) const
  {
    if (this->command != other.command) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotInit_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotInit_Request_

// alias to use template instance with default allocator
using RobotInit_Request =
  robot_interface::srv::RobotInit_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robot_interface


#ifndef _WIN32
# define DEPRECATED__robot_interface__srv__RobotInit_Response __attribute__((deprecated))
#else
# define DEPRECATED__robot_interface__srv__RobotInit_Response __declspec(deprecated)
#endif

namespace robot_interface
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct RobotInit_Response_
{
  using Type = RobotInit_Response_<ContainerAllocator>;

  explicit RobotInit_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sucess = false;
    }
  }

  explicit RobotInit_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sucess = false;
    }
  }

  // field types and members
  using _sucess_type =
    bool;
  _sucess_type sucess;

  // setters for named parameter idiom
  Type & set__sucess(
    const bool & _arg)
  {
    this->sucess = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robot_interface::srv::RobotInit_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const robot_interface::srv::RobotInit_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robot_interface::srv::RobotInit_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robot_interface::srv::RobotInit_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robot_interface::srv::RobotInit_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robot_interface::srv::RobotInit_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robot_interface::srv::RobotInit_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robot_interface::srv::RobotInit_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robot_interface::srv::RobotInit_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robot_interface::srv::RobotInit_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robot_interface__srv__RobotInit_Response
    std::shared_ptr<robot_interface::srv::RobotInit_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robot_interface__srv__RobotInit_Response
    std::shared_ptr<robot_interface::srv::RobotInit_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotInit_Response_ & other) const
  {
    if (this->sucess != other.sucess) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotInit_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotInit_Response_

// alias to use template instance with default allocator
using RobotInit_Response =
  robot_interface::srv::RobotInit_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robot_interface

namespace robot_interface
{

namespace srv
{

struct RobotInit
{
  using Request = robot_interface::srv::RobotInit_Request;
  using Response = robot_interface::srv::RobotInit_Response;
};

}  // namespace srv

}  // namespace robot_interface

#endif  // ROBOT_INTERFACE__SRV__DETAIL__ROBOT_INIT__STRUCT_HPP_
