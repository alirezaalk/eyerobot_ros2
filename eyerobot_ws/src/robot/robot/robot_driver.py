#! /usr/bin/env python3

from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

from geometry_msgs.msg import Pose
from std_msgs.msg import Float32
from std_msgs.msg import UInt16

import robot.com.lcm_ros_wrapper as lrw
import robot.com.robot_commands as rc
import time
import robot.excutor as re
import robot.composed as rcomp

class RobotDriver(Node):
    def __init__(self):
        super().__init__("robot_driver")
        self.get_logger().info("robot driver node is initilized!")
        self.counter = 0 
        self.topic_name = '/cmd_vel'
        self.driver_pub_topic = '/move_status'
        # self.robot_init = [i * 100000 for i in[1,1,1,1,1]]
        # self.move_status_pub = self.create_publisher(Float32, self.driver_pub_topic, 10)
        self.pose_subscriber = self.create_subscription(Pose, self.topic_name, self.pose_callback, 10)
        # self.timer_callback()
        self.gui_subscriber = self.create_subscription(UInt16, '/robot_init', self.gui_subcriber_callback, 10)
    def pose_callback(self, pose:Pose):
        move_status_msg = Float32()
        robot_pose = [pose.position.x, pose.position.y, pose.position.z, pose.orientation.x, pose.orientation.y]
        # self.get_logger().info(str(robot_pose))
        ### pose.oriention.z is the flag for mode
        signal = False
        move_status_msg.data = pose.orientation.z
        mode = pose.orientation.z
        print(mode)
        ######## TRAN ##############33
        if pose.orientation.z == 130.0:
            signal = rc.z_trans(robot_pose, direction = 1, dist = 100, speed = 25)
            rclpy.logging.get_logger(f"MoveForward-{str(mode)}").info(str(pose))
            if signal: move_status_msg = pose.orientation.z
            #self.move_status_pub.publish(move_status_msg)
            
        if pose.orientation.z == -130.0:
            signal = rc.z_trans(robot_pose, direction = -1, dist = 100, speed = 25)
            rclpy.logging.get_logger(f"MoveBackward-{str(mode)}").info(str(pose))
            if signal: move_status_msg = pose.orientation.z
            #self.move_status_pub.publish(move_status_msg)
            
        
        if pose.orientation.z == 130.1:
            signal = rc.y_trans(robot_pose, direction = 1, dist = 100, speed = 25)
            rclpy.logging.get_logger(f"MoveForward-{str(mode)}").info(str(pose))
            if signal: move_status_msg = pose.orientation.z
            #self.move_status_pub.publish(move_status_msg)
            
        if pose.orientation.z == -130.1:
            signal = rc.y_trans(robot_pose, direction = -1, dist = 100, speed = 25)
            rclpy.logging.get_logger(f"MoveBackward-{str(mode)}").info(str(pose))
            if signal: move_status_msg = pose.orientation.z
            #self.move_status_pub.publish(move_status_msg)

        if pose.orientation.z == 130.2:
            signal = rc.x_trans(robot_pose, direction = 1, dist = 100, speed = 25)
            rclpy.logging.get_logger(f"MoveForward-{str(mode)}").info(str(pose))
            if signal: move_status_msg = pose.orientation.z
            ##self.move_status_pub.publish(move_status_msg)

        if pose.orientation.z == -130.2:
            signal = rc.x_trans(robot_pose, direction = -1, dist = 100, speed = 25)
            rclpy.logging.get_logger(f"MoveBackward-{str(mode)}").info(str(pose))
            if signal: move_status_msg = pose.orientation.z
            ##self.move_status_pub.publish(move_status_msg)
        
        ############ RCM ###############
        if pose.orientation.z == 132.0:
            signal = rc.yz_rcm(robot_pose, direction = 1, dist = 100, speed = 25)
            rclpy.logging.get_logger(f"MoveForward-{str(mode)}").info(str(pose))
            if signal: move_status_msg = pose.orientation.z
            #self.move_status_pub.publish(move_status_msg)
            
        if pose.orientation.z == -132.0:
            signal = rc.yz_rcm(robot_pose, direction = -1, dist = 100, speed = 25)
            rclpy.logging.get_logger(f"MoveBackward-{str(mode)}").info(str(pose))
            if signal: move_status_msg = pose.orientation.z
            #self.move_status_pub.publish(move_status_msg)
            
        
        if pose.orientation.z == 132.1:
            signal = rc.xz_rcm(robot_pose, direction = 1, dist = 100, speed = 25)
            rclpy.logging.get_logger(f"MoveForward-{str(mode)}").info(str(pose))
            if signal: move_status_msg = pose.orientation.z
            #self.move_status_pub.publish(move_status_msg)
            
        if pose.orientation.z == -132.1:
            signal = rc.xz_rcm(robot_pose, direction = -1, dist = 100, speed = 25)
            rclpy.logging.get_logger(f"MoveBackward-{str(mode)}").info(str(pose))
            if signal: move_status_msg = pose.orientation.z
            #self.move_status_pub.publish(move_status_msg)

        if pose.orientation.z == 0.0:
            rc.stop_command()
        # if signal: move_status_msg = pose.orientation.z
        # #self.move_status_pub.publish(move_status_msg)
        print("publish is done")
    
    def gui_subcriber_callback(self, msg:UInt16):
        order_axis = ['z', 'x', 'y']
        if msg.data == 100:
            print(msg.data)
            rcomp.main()


        # for i in order_axis:
        #     try:
        #         print(i)

        #         # tran.main(default_init_pose[(order_axis.index(i))], i)
        #         return True
        #     except RuntimeError:
        #         print("some thing is wrong!")
        #         return False
        #         re.robot_init()

    
        
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