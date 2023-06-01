#! usr/bin/env python3
import rclpy
import numpy as np
from rclpy.node import Node
from robot_interface.srv import RobotInit
import robot.excutor as re

class RobotInitService(Node):
    def __init__(self):
        super().__init__("robot_services")
        self.get_logger().info("Service is initilized")
        self.srv = self.create_service(
            RobotInit, 
            'robot_init', 
            self.robot_init
            )

    def robot_init(self, request, response):
        
        if request.command == 100:
            
            try: 
                
                signal = re.robot_init()
                print("fo")
                print("do")
            except Exception as e:
                print('error', e)
                response.sucess = False
            response.sucess = True
        return response



def main(args=None):
    rclpy.init(args=args)

    node = RobotInitService()
    try:
        rclpy.spin(node=node)
        pass
    except SystemExit or KeyboardInterrupt:
        rclpy.logging.get_logger("Quitting").info("Done")
    node.destroy_node()
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()