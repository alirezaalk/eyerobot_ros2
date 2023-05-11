#! /usr/bin/env python3

from typing import List
import rclpy
from rclpy.context import Context
from rclpy.node import Node
from rclpy.parameter import Parameter

from geometry_msgs.msg import Pose


import lcm
from RobotMessage import RobotMessage 


class CalibMovement(Node):
    def __init__(self):
        super().__init__("calib_movement")
        self.get_logger().info("Node is initilized!")
        self.counter = 0 
        # self.init_cmd = self.create_publisher(Pose, '/init_rcm_cmd', 10)
        self.timer_callback()
    
    def timer_callback(self):
        ### setting up LCM
        lcm_rv = lcm.LCM()  #  receive status
        lcm_cm = lcm.LCM()  #  send command 
        message = RobotMessage()
        

        ## Setting up the target and encoders data
        target = [ 100000, 110000, 110000, 100000, 10000]
        message.control_bits = 132 # 132:RCM mode # 130: translational movement # 0 :stop

        for i in [(1,0), (0,1), (-1,0), (-1,-1)]:

            message.linear[0] = 0 ## in the code the z axis is set on other way
            message.linear[1] = -50       
            message.linear[2] = 0       
            message.nonlinear[0] = 0
            message.nonlinear[1] = 0
            message.nonlinear[2] = 0
            lcm_cm.publish("RobotCommand", message.encode())


        
def main(args=None):
    rclpy.init(args=args)

    node = CalibMovement()
    rclpy.spin(node=node)

    rclpy.shutdown()

if __name__ == "__main__":
    main()