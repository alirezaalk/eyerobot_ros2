#! /usr/bin/env python3

from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

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
            if robot_pose[3] < target and robot_pose[4] < target:
                feedback = [-130.2, 111.0, 0.0]
                pose.mode = -130.2
                self.cmd_slam_robot_pub.publish(pose)
                rclpy.logging.get_logger("move Forward_x").info(str(robot_pose))
                return feedback
            if robot_pose[3] > target and robot_pose[4] > target:
                feedback = [130.2, 111.0, 0.0]
                pose.mode = 130.2
                self.cmd_slam_robot_pub.publish(pose)
                rclpy.logging.get_logger("move backwar_x").info(str(robot_pose))
                return feedback

    
    def command_callback(self, cmd:RobotCommand):
        feedback  = RobotFeedback()
        ### Get the init Command
        if cmd.name == 'robot_init':
            speed = cmd.speed
            mode = round(cmd.mode,1)
            brake = cmd.stop_limit
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