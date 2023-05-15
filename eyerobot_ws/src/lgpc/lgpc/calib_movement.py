#! /usr/bin/env python3

from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

from geometry_msgs.msg import Pose

import lgpc.core.robot.lcm_ros_wrapper as lrw
import lgpc.core.robot.robot_commands as rc

class CalibMovement(Node):
    def __init__(self):
        super().__init__("calib_movement")
        self.get_logger().info("Node is initilized!!")
        self.counter = 0 
        self.topic_name = '/encoder_data'
        self.robot_init = [i * 100000 for i in[1,1,1,1,1]]
        # self.init_cmd = self.create_publisher(Pose, self.topic_name, 10)
        self.pose_subscriber = self.create_subscription(Pose, self.topic_name, self.pose_callback, 10)
        # self.timer_callback()
    
    def pose_callback(self, pose:Pose):
        robot_pose = [pose.position.x, pose.position.y, pose.position.z, pose.orientation.x, pose.orientation.y]
        signal = rc.rcm(robot_pose, -1 , 0)
        # signal = rc.z_trans(robot_pose, 10)
        if signal:
            raise SystemExit

        

    
        
def main(args=None):
    rclpy.init(args=args)

    node = CalibMovement()
    try:
        rclpy.spin(node=node)
    except:
        node.destroy_node()
        rclpy.logging.get_logger("Quitting").info("Movement is Done!")
        rclpy.shutdown()

if __name__ == "__main__":
    main()