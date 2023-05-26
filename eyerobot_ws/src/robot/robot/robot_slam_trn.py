#! /usr/bin/env python3

from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

from geometry_msgs.msg import Pose
import robot.com.lcm_ros_wrapper as lrw
import robot.com.robot_commands as rc

class RobotSLAMTrn(Node):
    def __init__(self , target, axis, stop_limit = 100):#, target):
        super().__init__("robot_slam_trn")
        self.get_logger().info("robot_slam_trn node is initilized!")
        self.counter = 0 
        self.pose_sub_topic= '/encoder_data'
        self.cmd_pub_topic = '/cmd_vel'
        self.robot_init = [i * 100000 for i in[1,1,1,1,1]]
        self.cmd_pub = self.create_publisher(Pose, self.cmd_pub_topic, 10)
        self.pose_sub = self.create_subscription(Pose, self.pose_sub_topic, self.pose_callback, 10)
        self.counter_ = 0
        self.target = target
        self.axis = axis
        self.stop_limit_ = 100
        # self.timer_callback()
    
    def pose_callback(self, pose:Pose):
        """
        mode definition: 
        the pose.orientation.z defines the mode and the direction
        + means forward - means backward (except for 1/2 (y) which is on the other way around)
        +- 130.X >> Translational 
            130.0 > z / 130.1 > y / 130.2 > x
        +- 132.X >> RCM
        0.0 >> Stop
        """
        robot_pose = [pose.position.x, pose.position.y, pose.position.z, pose.orientation.x, pose.orientation.y]
        #### actuator 0
        if self.axis == 'z':
            self.target = robot_pose + (self.target)
            if robot_pose[0] < self.target:
                pose.orientation.z = 130.0
                self.cmd_pub.publish(pose)
                rclpy.logging.get_logger("move Forward").info(str(robot_pose))
            if robot_pose[0] > self.target:
                pose.orientation.z = -130.0
                self.cmd_pub.publish(pose)
                rclpy.logging.get_logger("move backward").info(str(robot_pose))
            if abs(robot_pose[0] - self.target) < self.stop_limit_ :
                pose.orientation.z =  0.0
                rclpy.logging.get_logger("STOP").info(str(robot_pose))
                self.cmd_pub.publish(pose)
                raise SystemExit
        
        #### actuator 1 / 2
        if self.axis == 'y':
            if robot_pose[1] < self.target and robot_pose[2] < self.target:
                pose.orientation.z = -130.1
                self.cmd_pub.publish(pose)
                rclpy.logging.get_logger("move Forward").info(str(robot_pose))
            if robot_pose[1] > self.target and robot_pose[2] > self.target:
                pose.orientation.z = 130.1
                self.cmd_pub.publish(pose)
                rclpy.logging.get_logger("move backward").info(str(robot_pose))
            if abs(robot_pose[1] - self.target) < self.stop_limit_ and abs(robot_pose[2] - self.target) < self.stop_limit_:
                pose.orientation.z =  0.0
                rclpy.logging.get_logger("STOP").info(str(robot_pose))
                self.cmd_pub.publish(pose)
                raise SystemExit
            
         #### actuator 3 / 4
        if self.axis == 'x':
            if robot_pose[3] < self.target and robot_pose[4] < self.target:
                pose.orientation.z = -130.2
                self.cmd_pub.publish(pose)
                rclpy.logging.get_logger("move Forward").info(str(robot_pose))
            if robot_pose[3] > self.target and robot_pose[4] > self.target:
                pose.orientation.z = 130.2
                self.cmd_pub.publish(pose)
                rclpy.logging.get_logger("move backward").info(str(robot_pose))
            if abs(robot_pose[3] - self.target) < self.stop_limit_ and abs(robot_pose[4] - self.target) < self.stop_limit_:
                pose.orientation.z =  0.0
                rclpy.logging.get_logger("STOP").info(str(robot_pose))
                self.cmd_pub.publish(pose)
                raise SystemExit
 
        
def main(target = 140000, axis = 'y' ,args=None):
    rclpy.init(args=args)

    node = RobotSLAMTrn(target = target , axis= axis)
    try:
        rclpy.spin(node=node)
        pass
    except SystemExit:
        rclpy.logging.get_logger("Quitting").info("Done")
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main(target=140000)