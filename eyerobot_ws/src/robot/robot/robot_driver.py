#! /usr/bin/env python3

from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

from geometry_msgs.msg import Pose

import robot.core.robot.lcm_ros_wrapper as lrw
import robot.core.robot.robot_commands as rc

class RobotDriver(Node):
    def __init__(self):
        super().__init__("robot_driver")
        self.get_logger().info("robot driver node is initilized!")
        self.counter = 0 
        self.topic_name = '/cmd_vel'
        # self.robot_init = [i * 100000 for i in[1,1,1,1,1]]
        # self.cmd_to_lcm_pub = self.create_publisher(Pose, self.topic_name, 10)
        self.pose_subscriber = self.create_subscription(Pose, self.topic_name, self.pose_callback, 10)
        # self.timer_callback()
    
    def pose_callback(self, pose:Pose):
        robot_pose = [pose.position.x, pose.position.y, pose.position.z, pose.orientation.x, pose.orientation.y]
        self.get_logger().info(str(robot_pose))
        ### pose.oriention.z is the flag for mode
        
        mode = pose.orientation.z
        if pose.orientation.z == 130.0:
            signal = rc.z_trans(robot_pose, dist = 100, speed = 29)
        if pose.orientation.z == 0.0:
            rc.stop_command()
        # # How to kill a node with python
        # if signal:
        #     raise SystemExit



        
        

    
        
def main(args=None):
    rclpy.init(args=args)
    node = RobotDriver()
    try:
        rclpy.spin(node=node)
    except SystemExit:
        rclpy.logging.get_logger("Quitting").info("Done")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()