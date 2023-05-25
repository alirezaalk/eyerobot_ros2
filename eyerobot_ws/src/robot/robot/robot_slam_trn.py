#! /usr/bin/env python3

from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

from geometry_msgs.msg import Pose
import robot.core.robot.lcm_ros_wrapper as lrw
import robot.core.robot.robot_commands as rc

class RobotSLAMTrn(Node):
    def __init__(self ):#, target):
        super().__init__("robot_slam_trn")
        self.get_logger().info("robot_slam_trn node is initilized!")
        self.counter = 0 
        self.pose_sub_topic= '/encoder_data'
        self.cmd_pub_topic = '/cmd_vel'
        self.robot_init = [i * 100000 for i in[1,1,1,1,1]]
        self.cmd_pub = self.create_publisher(Pose, self.cmd_pub_topic, 10)
        self.pose_sub = self.create_subscription(Pose, self.pose_sub_topic, self.pose_callback, 10)
        self.counter_ = 0
        #self.target = target
        # self.timer_callback()
    
    def pose_callback(self, pose:Pose):
        robot_pose = [pose.position.x, pose.position.y, pose.position.z, pose.orientation.x, pose.orientation.y]
        self.target =  120000
        if robot_pose[0] < 120000:
            pose.orientation.z = 130.0
            self.counter_ += 1
            self.get_logger().info(str(robot_pose))
            self.cmd_pub.publish(pose)
        if robot_pose[0] > 120000:
            pose.orientation.z = 0.0
            self.cmd_pub.publish(pose)
            raise SystemExit
        
        
        
        # # How to kill a node with python
        # if signal:
        #     raise SystemExit
 
        
def main(args=None):
    rclpy.init(args=args)

    node = RobotSLAMTrn()
    try:
        rclpy.spin(node=node)
        pass
    except SystemExit:
        rclpy.logging.get_logger("Quitting").info("Done")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()