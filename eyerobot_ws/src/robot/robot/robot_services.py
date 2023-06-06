#! usr/bin/env python3
import rclpy
import numpy as np
from rclpy.node import Node
from robot_interface.srv import RobotCom
import robot.excutor as re
import threading
import rclpy
from robot.robot_slam_trn import RobotSLAMTrn
from rclpy.executors import MultiThreadedExecutor


class RobotInitService(Node):
    def __init__(self):
        super().__init__("robots_services")
        self.get_logger().info("Service is initilized")
        self.srv = self.create_service(
            RobotCom, 
            'robot_command', 
            self.robot_command
            )
        
        
        
    def robot_command(self, request, response):
        speed = request.speed
        stop_limit = request.stop_limit
        target = request.coordinate
        command = request.name
        if request.mode == 100.0:
            
            # trn = RobotSLAMTrn(target = 110000.0, axis = 'z', speed= 24)
            try: 
                
                #trn = RobotSLAMTrn(target = 110000.0, axis = 'z', speed= 24)
                # self.executor.add_node(trn)

                signal = re.robot_init(speed=speed)
                # rclpy.spin()
                # executor_thread = threading.Thread(target=self.executor.spin, daemon=True)
                # executor_thread.start()
                # rate = trn.create_rate(2)
                #print(rate)
                # try:
                    # while rclpy.ok():
                    #     print('Help me body, you are my only hope')
                    #     rate.sleep()
                    # self.executor.spin()
                # except KeyboardInterrupt:
                #     pass
                # rclpy.shutdown()
            #finally:
                    # self.executor.shutdown()
                    # trn.destroy_node()
                    # executor_thread.join()
                
                print("fo")
                print("do")
                response.result = 'True'
            except Exception as e:
                print('error', e)
                response.result = 'False'
            
            print(response.result)
        return response

def main(args=None):
    rclpy.init(args=args)

    node = RobotInitService()
    try:
        rclpy.spin(node=node)
        pass
    except KeyboardInterrupt:
        rclpy.logging.get_logger("Quitting").info("Done")
    node.destroy_node()
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()