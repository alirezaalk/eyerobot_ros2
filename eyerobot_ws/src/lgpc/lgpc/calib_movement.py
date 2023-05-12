#! /usr/bin/env python3

from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

from geometry_msgs.msg import Pose
import lcm_ros_wrapper as lrw
import lcm
from RobotMessage import RobotMessage 


class CalibMovement(Node):
    def __init__(self):
        super().__init__("calib_movement")
        self.get_logger().info("Node is initilized!")
        self.counter = 0 
        self.init_cmd = self.create_publisher(Pose, '/init_rcm_cmd', 10)
        self.pose_subscriber = self.create_subscription(Pose, "/robot_encoder", self.pose_callback, 10)
        # self.timer_callback()
    
    def pose_callback(self, pose:Pose):
        pose, _ = lrw.encoder_data()
        print(pose)
        

    
        
def main(args=None):
    rclpy.init(args=args)

    node = CalibMovement()
    rclpy.spin(node=node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()