#! /usr/bin/env python3

import robot.robot_slam_rcm as rcm
import robot.robot_slam_trn as tran



def robot_init(default_init_pose=[100000,100000,100000], order_axis = ['z', 'x', 'y']):
    """
    robot initlizing function
    paramters: 
        - default_init_pose : the initilizing pose of the needle
        - order_axis : the order of initilizing
    return:
        - true: the initilizing is done
        - false : there is an error

    """
    # for i in order_axis:
        # try:
        #     print(i)
        #     tran.main(default_init_pose[(order_axis.index(i))], i)
        #     return True
        # except RuntimeError:
        #     print("some thing is wrong!")
        #     return False
    tran.main(120000, 'z')
if __name__ == '__main__':
    robot_init()