#! /usr/bin/env python3

from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter
import numpy as np
from geometry_msgs.msg import Pose
from robot_interface.msg import RobotPose
from robot_interface.msg import RobotCommand
from robot_interface.msg import RobotFeedback
from std_msgs.msg import Float32
import robot.com.lcm_ros_wrapper as lrw
import robot.com.robot_commands as rc
import sys
import robot.excutor as re
class RobotSLAM(Node):
    def __init__(self):#  , target, axis, speed= 25, stop_limit = 100):#, target):
        super().__init__("robot_slam")
        self.get_logger().info("robot_slam node is initilized!")
        self.counter = 0 
        self.pose = RobotPose()
        self.pose_sub_topic= '/encoder_data'
        self.cmd_slam_robot_pub_topic = '/cmd_vel'
        self.driver_pub_topic = '/move_status'
        self.signal_gui_pub_topic = '/slam_feedback'
        self.command_sub_topic = '/cmd_pose'
        self.robot_init = [i * 100000 for i in[1,1,1,1,1]]
        self.cmd_slam_robot_pub = self.create_publisher(
            RobotPose, 
            self.cmd_slam_robot_pub_topic,
            10)
        self.pose_sub = self.create_subscription(
            RobotPose, 
            self.pose_sub_topic, 
            self.pose_callback, 
            10)
        self.result = 'None'
        
        self.feedback_slam_gui_pub = self.create_publisher(
            RobotFeedback, 
            self.signal_gui_pub_topic, 
            10)
        
        self.command_gui_slam_sub = self.create_subscription(
            RobotCommand, 
            self.command_sub_topic,
            self.command_callback,
            10)
        self.counter_ = 0
        self.robot_pose = [0,0,0,0,0]
        self.axis = ''
        self.stop_limit_ = 5000
        self.robot_speed = 0
        self.targetpose = [0,0,0,0,0]
        self.deg_xz = 0
        self.deg_yz = 0

    def feedback_slam_gui(self):
        feedback = RobotFeedback()
        pass

    def trn_move(self, curr_pose, target, speed, brake, axis):
        pose = RobotPose()
        pose.speed = speed
        robot_pose  = curr_pose
        if axis == 130.0:
            if abs(robot_pose[0] - target) < brake :
                feedback = [130.0, 100.0, 0.0]
                pose.mode = 0.0
                pose.speed = 0
                rclpy.logging.get_logger("STOP").info(str(robot_pose))
                self.cmd_slam_robot_pub.publish(pose)
                return feedback
            if robot_pose[0] < target:
                feedback = [130.0, 111.0, 0.0]
                pose.mode = 130.0
                self.cmd_slam_robot_pub.publish(pose)
                rclpy.logging.get_logger(f"move Forward_{axis}").info(str(robot_pose))
                return feedback
            if robot_pose[0] > target:
                feedback = [-130.0, 111.0, 0.0]
                pose.mode = -130.0
                self.cmd_slam_robot_pub.publish(pose)
                rclpy.logging.get_logger(f"move backward_{axis}").info(str(robot_pose))
                return feedback
            
       
        if axis == 130.1:
            if abs(robot_pose[1] - target) < brake and abs(robot_pose[2] - target) < brake:
                feedback = [130.1, 100.0, 0.0]
                pose.mode = 0.0
                pose.speed = 0
                rclpy.logging.get_logger("STOP").info(str(robot_pose))
                return feedback
            if robot_pose[1] < target and robot_pose[2] < target:
                feedback = [-130.1, 111.0, 0.0]
                pose.mode = -130.1
                self.cmd_slam_robot_pub.publish(pose)
                rclpy.logging.get_logger("move Forward_y").info(str(robot_pose))
                return feedback
            if robot_pose[1] > target and robot_pose[2] > target:
                feedback = [130.1, 111.0, 0.0]
                pose.mode = 130.1
                self.cmd_slam_robot_pub.publish(pose)
                rclpy.logging.get_logger("move backwar_y").info(str(robot_pose))
                return feedback
                
        if axis == 130.2:
            if abs(robot_pose[3] - target) < brake and abs(robot_pose[4] - target) < brake:
                feedback = [130.2, 100.0, 0.0]
                pose.mode = 0.0
                pose.speed = 0
                rclpy.logging.get_logger("STOP").info(str(robot_pose))
                return feedback
            
            ## TODO some times we need to add rcm in order to initilize. because the old movemet was RCM and can not be initilized just by checking these two
            ## TODO in order to solve: first initlize the parallel joints (130.1 and 130.2) and then z (130.0)
            """
            if abs(robot_pose[3] - target) < brake or abs(robot_pose[4] - target) < brake:
                if abs(robot_pose[3] - target) > brake:
                    feedback = [-130.2, 111.0, 0.0]
                    pose.mode = -132.1
                    self.cmd_slam_robot_pub.publish(pose)
                if abs(robot_pose[4] - target) > brake:
                    feedback = [-130.2, 111.0, 0.0]
                    pose.mode = 132.1
                    self.cmd_slam_robot_pub.publish(pose)
            """
            if robot_pose[3] < target and robot_pose[4] < target:
                feedback = [-130.2, 111.0, 0.0]
                pose.mode = -130.2
                self.cmd_slam_robot_pub.publish(pose)
                rclpy.logging.get_logger("move Forward_x").info(str(self.robot_pose))
                return feedback
            if robot_pose[3] > target and robot_pose[4] > target:
                feedback = [130.2, 111.0, 0.0]
                pose.mode = 130.2
                self.cmd_slam_robot_pub.publish(pose)
                rclpy.logging.get_logger("move backwar_x").info(str(robot_pose))
                return feedback

    def target_calculator(self, robot_pose, xz_deg= 0, yz_deg= 0):
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
    
    def rcm_move(self, curr_pose, target, deg_xz, deg_yz, speed, axis, brake = 5000):
            pose = RobotPose()
            print('target', target)
            print('deg', deg_xz)
            print('deg_yz', deg_yz)
            pose.speed = speed
            robot_pose = curr_pose
            #if robot_pose[0] < self.target[0] and robot_pose[1] < self.target[1] and robot_pose[2]< self.target[2]:
            if axis == 132.0:
                diff = [abs(robot_pose[0] - target[0]), abs(robot_pose[1] - target[1]), abs(robot_pose[2] - target[2])]
                if (abs(robot_pose[0] - target[0]) < brake) or  (abs(robot_pose[1] - target[1]) < brake or abs(robot_pose[2] - target[2]) < brake):
                    # data.data = pose.orientation.z
                    feedback = [132.0, 100.0, 1.0]             
                    pose.mode = 0.0
                    pose.speed = 0
                    rclpy.logging.get_logger("STOP").info(str(robot_pose))
                    self.cmd_slam_robot_pub.publish(pose)
                    return feedback
                    # rclpy.logging.get_logger("STOP").info(str(robot_pose))
                    # self.cmd_pub.publish(pose)
                if deg_yz >= 0:
                    feedback = [132.0, 111.0, 1.0]             
                    pose.mode = -132.0
                    pose.speed = 20
                    rclpy.logging.get_logger("backward_yz").info(str(robot_pose))
                    self.cmd_slam_robot_pub.publish(pose)
                    return feedback
        
                if deg_yz < 0:
                    feedback = [132.0, 111.0, 1.0] 
                    pose.mode = 132.0
                    self.cmd_slam_robot_pub.publish(pose)
                    rclpy.logging.get_logger("forkward_yz").info(str(robot_pose))
                    return feedback
                
            ## XZ / act 3,4 
            
            if axis == 132.1:
                diff = [abs(robot_pose[0] - target[0]), abs(robot_pose[3] - target[3]), abs(robot_pose[4] - target[4])]
                if (abs(robot_pose[0] - target[0]) < brake ) or  (abs(robot_pose[3] - target[3]) < brake or abs(robot_pose[4] - target[4]) < brake):
                
                    # data.data = pose.orientation.z
                    pose.mode = 0.0
                    pose.speed = 0
                    feedback = [132.1, 100.0, 1.0]             
                    rclpy.logging.get_logger("STOP").info(str(diff))
                    self.cmd_slam_robot_pub.publish(pose)
                    return feedback
                    # rclpy.logging.get_logger("STOP").info(str(robot_pose))
                    # self.cmd_pub.publish(pose)
                if deg_xz > 0:
                    feedback = [132.1, 111.0, 1.0]             
                    pose.mode = -132.1
                    pose.speed = 20
                    rclpy.logging.get_logger("backward_xz").info(str(diff))
                    self.cmd_slam_robot_pub.publish(pose)
                    return feedback
        
                if deg_xz < 0:
                    feedback = [132.1, 111.0, 1.0] 
                    pose.mode = 132.1
                    pose.speed = 20
                    self.cmd_slam_robot_pub.publish(pose)
                    rclpy.logging.get_logger("forward_xz").info(str(robot_pose))
                    return feedback
            
    
    def command_callback(self, cmd:RobotCommand):

        feedback  = RobotFeedback()
        mode = round(cmd.mode,1)
        brake = cmd.stop_limit
        speed = cmd.speed
        feedback.key.x = 0.0
        feedback.key.y = 0.0

        print(self.robot_pose)
        ### GROBOT INITILIZATION
        if cmd.name == 'robot_init' :
            target_z = cmd.coordinate.position.z
            target_y = cmd.coordinate.position.y
            target_x = cmd.coordinate.position.x
            rclpy.logging.get_logger(f"Recieved_{mode}_{speed}_{brake}_{target_z}").info(cmd.name)
            if mode == 130.0 :
                result = self.trn_move(self.robot_pose, target_z, speed=speed, brake=brake, axis= mode )
                print(result)
                feedback.name = cmd.name
                feedback.key.x = result[0]
                feedback.key.y = result[1]
                self.feedback_slam_gui_pub.publish(feedback)

            if mode == 130.1 :
                result = self.trn_move(self.robot_pose, target_y, speed=speed, brake=brake, axis= mode )
                feedback.name = cmd.name
                feedback.key.x = result[0]
                feedback.key.y = result[1]
                self.feedback_slam_gui_pub.publish(feedback)
            
            if mode == 130.2 :
                result = self.trn_move(self.robot_pose, target_x, speed=speed, brake=brake, axis= mode )
                feedback.name = cmd.name
                feedback.key.x = result[0]
                feedback.key.y = result[1]
                self.feedback_slam_gui_pub.publish(feedback)
            if mode == 0.0:
                rc.stop_command()
                feedback.name = 'Standby'
                feedback.key.x = 0.0
                feedback.key.y = 0.0
                self.feedback_slam_gui_pub.publish(feedback)
        
        ## ROBOT CALIBRATION (RCM ROUND)
        if cmd.name == 'robot_calib' or cmd.name == 'robot_calib_r':
            self.targetpose = [cmd.target0, cmd.target1,cmd.target2,cmd.target3,cmd.target4]
            self.deg_xz = cmd.coordinate.orientation.x
            self.deg_yz = cmd.coordinate.orientation.y
            speed = 20

            # RCM YZ
            if mode == 132.0:
                # print("RCM YZ", self.robot_pose)
                # print(self.targetpose)
                result = self.rcm_move(self.robot_pose, self.targetpose, deg_xz = self.deg_xz, deg_yz = self.deg_yz, speed=speed,  axis= mode )
                feedback.name = cmd.name
                feedback.key.x = mode
                feedback.key.y = result[1]
                self.feedback_slam_gui_pub.publish(feedback)
            ## RCM XZ
            if mode == 132.1:
                # print("RCM XZ")
                # print(self.targetpose)
                result = self.rcm_move( self.robot_pose, self.targetpose, deg_xz = self.deg_xz, deg_yz = self.deg_yz, speed=speed, brake=5000, axis= mode )
                feedback.name = cmd.name
                feedback.key.x = mode
                feedback.key.y = result[1]
                self.feedback_slam_gui_pub.publish(feedback)
            if mode == 0.0:
                rc.stop_command()
                feedback.name = 'Standby'
                feedback.key.x = 0.0
                feedback.key.y = 0.0
                self.feedback_slam_gui_pub.publish(feedback)


    def pose_callback(self, pose:RobotPose):
        try:
            """
            mode definition: 
            the pose.orientation.z defines the mode and the direction
            + means forward - means backward (except for 1/2 (y) which is on the other way around)
            +- 130.X >> Translational 
                130.0 > z / 130.1 > y / 130.2 > x
            +- 132.X >> RCM
            0.0 >> Stop
            """
            self.robot_pose = [pose.en0, pose.en1, pose.en2, pose.en3, pose.en4]    
        except SystemExit:
            rc.stop_command()
            rclpy.logging.get_logger("Quitting!").info("Done")





def main(target = 108000, speed = 10,  axis = 'z' ,args=None):
    rclpy.init(args=args)
    # print(str(sys.argv[1]))
    node = RobotSLAM()
    try:
        rclpy.spin(node=node)
        
    except SystemExit:
        rc.stop_command()

        rclpy.logging.get_logger("Quitting!").info("Done")
        node.destroy_node()
        rclpy.shutdown()
        return True
    except KeyboardInterrupt:
        rc.stop_command()
        rclpy.logging.get_logger("Quitting!").info("Done")
        node.destroy_node()
        rclpy.shutdown()
        return False

    


if __name__ == "__main__":
    result = main(target=140000)
    print(result)