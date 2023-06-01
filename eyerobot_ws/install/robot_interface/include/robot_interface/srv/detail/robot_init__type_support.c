// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robot_interface:srv/RobotInit.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robot_interface/srv/detail/robot_init__rosidl_typesupport_introspection_c.h"
#include "robot_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robot_interface/srv/detail/robot_init__functions.h"
#include "robot_interface/srv/detail/robot_init__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_interface__srv__RobotInit_Request__init(message_memory);
}

void RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_fini_function(void * message_memory)
{
  robot_interface__srv__RobotInit_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_message_member_array[1] = {
  {
    "command",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_interface__srv__RobotInit_Request, command),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_message_members = {
  "robot_interface__srv",  // message namespace
  "RobotInit_Request",  // message name
  1,  // number of fields
  sizeof(robot_interface__srv__RobotInit_Request),
  RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_message_member_array,  // message members
  RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_message_type_support_handle = {
  0,
  &RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interface, srv, RobotInit_Request)() {
  if (!RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_message_type_support_handle.typesupport_identifier) {
    RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &RobotInit_Request__rosidl_typesupport_introspection_c__RobotInit_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_interface/srv/detail/robot_init__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_interface/srv/detail/robot_init__functions.h"
// already included above
// #include "robot_interface/srv/detail/robot_init__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_interface__srv__RobotInit_Response__init(message_memory);
}

void RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_fini_function(void * message_memory)
{
  robot_interface__srv__RobotInit_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_message_member_array[1] = {
  {
    "sucess",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_interface__srv__RobotInit_Response, sucess),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_message_members = {
  "robot_interface__srv",  // message namespace
  "RobotInit_Response",  // message name
  1,  // number of fields
  sizeof(robot_interface__srv__RobotInit_Response),
  RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_message_member_array,  // message members
  RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_message_type_support_handle = {
  0,
  &RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interface, srv, RobotInit_Response)() {
  if (!RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_message_type_support_handle.typesupport_identifier) {
    RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &RobotInit_Response__rosidl_typesupport_introspection_c__RobotInit_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "robot_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "robot_interface/srv/detail/robot_init__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers robot_interface__srv__detail__robot_init__rosidl_typesupport_introspection_c__RobotInit_service_members = {
  "robot_interface__srv",  // service namespace
  "RobotInit",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // robot_interface__srv__detail__robot_init__rosidl_typesupport_introspection_c__RobotInit_Request_message_type_support_handle,
  NULL  // response message
  // robot_interface__srv__detail__robot_init__rosidl_typesupport_introspection_c__RobotInit_Response_message_type_support_handle
};

static rosidl_service_type_support_t robot_interface__srv__detail__robot_init__rosidl_typesupport_introspection_c__RobotInit_service_type_support_handle = {
  0,
  &robot_interface__srv__detail__robot_init__rosidl_typesupport_introspection_c__RobotInit_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interface, srv, RobotInit_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interface, srv, RobotInit_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_interface
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interface, srv, RobotInit)() {
  if (!robot_interface__srv__detail__robot_init__rosidl_typesupport_introspection_c__RobotInit_service_type_support_handle.typesupport_identifier) {
    robot_interface__srv__detail__robot_init__rosidl_typesupport_introspection_c__RobotInit_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)robot_interface__srv__detail__robot_init__rosidl_typesupport_introspection_c__RobotInit_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interface, srv, RobotInit_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interface, srv, RobotInit_Response)()->data;
  }

  return &robot_interface__srv__detail__robot_init__rosidl_typesupport_introspection_c__RobotInit_service_type_support_handle;
}
