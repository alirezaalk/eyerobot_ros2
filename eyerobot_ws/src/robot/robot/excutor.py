#! /usr/bin/env python3

import robot.robot_slam_rcm as rcm


import rclpy
import numpy as np
from rclpy.node import Node
from robot_interface.srv import RobotCom
import robot.excutor as re
import threading
import rclpy

from rclpy.executors import MultiThreadedExecutor


# executor.shutdown()
def robot_init(default_init_pose=[100000,100000,100000], speed=30, order_axis = ['y', 'z', 'x']):
    """
    robot initlizing function
    paramters: 
        - default_init_pose : the initilizing pose of the needle
        - order_axis : the order of initilizing
    return:
        - true: the initilizing is done
        - false : there is an error

    """

    # executor = MultiThreadedExecutor()
    # for i in order_axis:
    #     print(i)
        # trn = RobotSLAMTrn(default_init_pose[(order_axis.index(i))],speed=speed, axis=i)
    trn1 = tr.main(target = 120000.0, axis = 'z')
    print(trn1)
    
        # executor.add_node(trn)
        # executor_thread = threading.Thread(target=executor.spin, daemon=True)
        # executor_thread.start()
        # rate = trn.create_rate(2)
        # print(rate)
        # try:
        #     while rclpy.ok():
        #         print('Help me body, you are my only hope')
        #         rate.sleep()
        #         executor.spin()
        # except KeyboardInterrupt:    
        #     executor.shutdown()
        #     trn.destroy_node()
        #     executor_thread.join()

        
    # try:
    #     for i in order_axis:
    #         print(i)
    #         tran.main(default_init_pose[(order_axis.index(i))],speed=speed, axis=i)
    #         print(default_init_pose[(order_axis.index(i))])
    #     return 'True'
    # except RuntimeError:
    #     print("some thing is wrong!")

    
if __name__ == '__main__':
    robot_init()