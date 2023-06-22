#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from robot_interface.msg import RobotPose
from robot_interface.msg import RobotJoystick

class InputRobotInterface(Node):
    def __init__(self):
        super().__init__("input_robot_interface")
        self.get_logger().info("Joystik Robot Interface node has been stablished!")

        self.input_node_sub = self.create_subscription(RobotJoystick, '/input_signal', self.input_callback, 10)
        self.interface_robot_pub = self.create_publisher(RobotPose, '/cmd_vel', 10 )
    

    def input_callback(self, rec_signal:RobotJoystick):
        pub_cmd = RobotPose()
        self.mode = round(rec_signal.mode,1)
        self.speed = rec_signal.speed
        self.mode_name = rec_signal.mode_name
        self.get_logger().info(f'Input_Signal: {self.mode_name}/ Code: {self.mode}/ Speed: {self.speed}')
        pub_cmd.mode = self.mode
        pub_cmd.speed = self.speed
        self.interface_robot_pub.publish(pub_cmd)


def main(args = None):
    rclpy.init(args=args)
    node = InputRobotInterface()
    try:
        rclpy.spin(node=node)
    except KeyboardInterrupt:
        rclpy.logging.get_logger("Quitting!").info('Quit Done')
        node.destroy_node()
        rclpy.shutdown()
