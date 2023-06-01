#! /usr/bin/env python3

import numpy as np
from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

from robot_interface.msg import RobotPose
from std_msgs.msg import Float32
import robot.com.lcm_ros_wrapper as lrw
import robot.com.robot_commands as rc

class RobotSLAMRcm (Node):
    def __init__(self , target_deg, axis, speed = 25, stop_limit = 100):#, target):
        super().__init__("robot_slam_rcm")
        self.get_logger().info("robot_slam_rcm node is initilized!")
        self.counter = 0 
        self.pose_sub_topic= '/encoder_data'
        self.cmd_pub_topic = '/cmd_vel'
        self.driver_pub_topic = '/move_status'
        self.robot_init = [i * 100000 for i in[1,1,1,1,1]]
        self.cmd_pub = self.create_publisher(RobotPose, self.cmd_pub_topic, 10)
        self.pose_sub = self.create_subscription(RobotPose, self.pose_sub_topic, self.pose_callback, 10)
        self.move_status_pub = self.create_publisher(RobotPose, self.driver_pub_topic, 10)
        self.counter_ = 0
        # [target_deg_xz, target_deg_yz]
        self.target_deg = target_deg
        self.axis = axis
        self.stop_limit_ = 100
        self.counter_  = 0
        self.robot_speed = speed
        # self.timer_callback()
    

    # def target_calculator(self,  xz_deg= 0, yz_deg= 0):
    #     xz_deg = self.target_deg[0]
    #     yz_deg = self.target_deg[1]
    #     link1 = 29.5
    #     link2 = 49.0
    #     offset1 = 4.75
    #     offsexz_deg = 19
    #     Ltool = 88.90
    #     rcmlength = 20
    #     DISTANCE_SLIDE=230000
    #     target = [-(Ltool - rcmlength), link2, link1-offsexz_deg]
    #     d5 = (target[0] + offsexz_deg * np.sin(xz_deg) + offset1 * np.cos(xz_deg) + link2 * np.cos(xz_deg) * np.sin(yz_deg) - link1 * np.sin(xz_deg)) / (-np.cos(xz_deg) * np.cos(yz_deg))
    #     d3 =  target[1] + d5 * np.sin(yz_deg) - link2 * np.cos(yz_deg)
    #     d1 =  target[2] - d5 * np.sin(xz_deg) * np.cos(yz_deg) - link1 * np.cos(xz_deg) - link2 * np.sin(xz_deg) * np.sin(yz_deg) - offset1 * np.sin(xz_deg) + offsexz_deg * np.cos(xz_deg)
    #     targetpos = [0,0,0,0,0]
    #     targetpos[0] =  (d5 + target[0] + offset1) * 10000.0
    #     targetpos[2] = 100000 - d3 * 10000.0
    #     targetpos[1] = targetpos[2] - DISTANCE_SLIDE * np.tan(yz_deg)
    #     targetpos[4] = 100000 - d1 * 10000.0
    #     targetpos[3] = targetpos[4] + DISTANCE_SLIDE * np.tan(xz_deg)
    #     return targetpos #, d5, d3, d1

    def pose_callback(self, pose:RobotPose):
        """
        mode definition: 
        the pose.orientation.z defines the mode and the direction
        + means forward - means backward (except for 1/2 (y) which is on the other way around)
        +- 130.X >> Translational 
            130.0 > z / 130.1 > y / 130.2 > x
        +- 132.X >> RCM mode 
            132.0 > xz / 132.1 > yz 
        0.0 >> Stop
        """
        self.counter_ += 1
        print(self.counter_)
        robot_pose = [pose.en0, pose.en1, pose.en2, pose.en3, pose.en4]
        pose.speed = self.robot_speed
        #### actuator 1 / 2
        xz_deg = self.target_deg[0]
        yz_deg = self.target_deg[1]
        if self.counter_ == 1:
            self.target = target_calculator(robot_pose , xz_deg= xz_deg , yz_deg= yz_deg)
            #self.target = self.target + robot_pose
        # print(robot_pose)
        if self.axis == 'yz':
            print(self.target)
            #if robot_pose[0] < self.target[0] and robot_pose[1] < self.target[1] and robot_pose[2]< self.target[2]:
            if self.target_deg[1] > 0:
                pose.mode = -132.0
                
                self.cmd_pub.publish(pose)
                rclpy.logging.get_logger("move Forward").info(str(robot_pose))
            #if robot_pose[0] > self.target[0] and robot_pose[1] > self.target[1] and robot_pose[2] > self.target[2]:
            if self.target_deg[1] < 0:
                pose.mode = 132.0
                self.cmd_pub.publish(pose)
                rclpy.logging.get_logger("move backward").info(str(robot_pose))
            if (abs(robot_pose[0] - self.target[0]) < self.stop_limit_) or  (abs(robot_pose[1] - self.target[1]) < self.stop_limit_ or abs(robot_pose[2] - self.target[2]) < self.stop_limit_):
                # data.data = pose.orientation.z
                self.move_status_pub.publish(pose)
                pose.mode =  0.0
                rclpy.logging.get_logger("STOP").info(str(robot_pose))
                self.cmd_pub.publish(pose)
                raise SystemExit
            
         #### actuator 3 / 4
        if self.axis == 'xz':
            # self.target = [i/10 for i in self.target]
            # self.target[0] = self.target[0]/10
            # self.target[1] = self.target[1]/10
            # self.target[2] = self.target[0]/10
            
            
            diff = [abs(robot_pose[0] - self.target[0]), abs(robot_pose[3] - self.target[3]), abs(robot_pose[4] - self.target[4])]
            print(self.target)
            #if robot_pose[0] < self.target[0] and robot_pose[3] < self.target[3] and robot_pose[4]< self.target[4]:
            if self.target_deg[0] > 0 :
                pose.mode = -132.1
                self.cmd_pub.publish(pose)
                rclpy.logging.get_logger("move Forward").info(str(diff))
            #if robot_pose[0] > self.target[0] and robot_pose[3] > self.target[3] and robot_pose[4] > self.target[4]:
            if self.target_deg[0] < 0:
                pose.mode = 132.1
                self.cmd_pub.publish(pose)
                rclpy.logging.get_logger("move backward").info(str(diff))
            if (abs(robot_pose[0] - self.target[0]) < self.stop_limit_ ) or  (abs(robot_pose[3] - self.target[3]) < self.stop_limit_ or abs(robot_pose[4] - self.target[4]) < self.stop_limit_):
                # data.data = pose.orientation.z
                
                self.move_status_pub.publish(pose)
                pose.mode =  0.0
                rclpy.logging.get_logger("STOP").info(str(robot_pose))
                self.cmd_pub.publish(pose)
                
                raise SystemExit



def target_calculator(robot_pose, xz_deg= 0, yz_deg= 0):
        xz_deg = xz_deg/-180*np.pi
        yz_deg = yz_deg/-180*np.pi
        link1 = 29.5
        link2 = 49.0
        offset1 = 4.75
        offsexz_deg = 19
        Ltool = 88.90
        rcmlength = 20
        DISTANCE_SLIDE=230000
        target = [-(Ltool - rcmlength), link2, link1-offsexz_deg]
        d5 = (target[0] + offsexz_deg * np.sin(xz_deg) + offset1 * np.cos(xz_deg) + link2 * np.cos(xz_deg) * np.sin(yz_deg) - link1 * np.sin(xz_deg)) / (-np.cos(xz_deg) * np.cos(yz_deg))
        d3 =  target[1] + d5 * np.sin(yz_deg) - link2 * np.cos(yz_deg)
        d1 =  target[2] - d5 * np.sin(xz_deg) * np.cos(yz_deg) - link1 * np.cos(xz_deg) - link2 * np.sin(xz_deg) * np.sin(yz_deg) - offset1 * np.sin(xz_deg) + offsexz_deg * np.cos(xz_deg)
        targetpos = [0,0,0,0,0]
        targetpos[0] =  (d5 + target[0] + offset1) * 10000.0
        targetpos[2] =  robot_pose[2]- d3 * 10000.0
        targetpos[1] = targetpos[2] - DISTANCE_SLIDE * np.tan(yz_deg)
        targetpos[4] =  robot_pose[4] - d1 * 10000.0
        targetpos[3] = targetpos[4] + DISTANCE_SLIDE * np.tan(xz_deg)
        return targetpos# , d5, d3, d1

        
def main(target = [0,-0.6], axis = 'yz' ,args=None):
    rclpy.init(args=args)
    node = RobotSLAMRcm(target_deg = target , axis= axis)
    
    try:
        rclpy.spin(node=node)
        pass
    except SystemExit or KeyboardInterrupt:
        rclpy.logging.get_logger("Quitting").info("Done")
    node.destroy_node()
    rclpy.shutdown()
    


if __name__ == "__main__":
    robot_pose = [70000, 100000, 100000, 100000, 100000]
    # main(target=[0,3], axis= "yz")
    print(target_calculator(robot_pose, 0, 1.1))