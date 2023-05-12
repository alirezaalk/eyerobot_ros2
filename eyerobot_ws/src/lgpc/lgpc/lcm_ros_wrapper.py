import lcm 
import time
from lgpc.RobotMessage import RobotMessage
import math
from io import BytesIO
import signal
import struct
import ctypes

lcm_rv = lcm.LCM()  #  receive status
lcm_cm = lcm.LCM()  #  send command 
message = RobotMessage()
"""
These methods helps to decode and encode encoders data with using lcm for later usage in ros2
"""

def data_subscription(channel, data):
    """
    subscribe the data in lcm channel
    parameters:
    ----------
    data : LCMSubcription
        data recieved and needs to be decoded 
    msg : decoded data 
    """
    global encoder_pose, encoder_vel, rv_mode, lin_data, nonlin_data
    msg = RobotMessage.decode(data)
    encoder_pose = msg.position
    encoder_vel = msg.velocity
    rv_mode = msg.control_bits
    lin_data = msg.linear
    nonlin_data = msg.nonlinear
    

def data_publisher(mode, speed, robot_cmd):
    """
    publishing commands through the lcm
    parameters: 
    --------
    speed : int 
        defines the speed of the movement from 0 to 1 mm/s
    robot_cmd: array [z, y , x]
        includes the planes in rcm movement and direction in translational movement
        
    """
    lcm_cm = lcm.LCM()  #  send command 
    robot_cmd = [item * speed for item in robot_cmd] 
    print(robot_cmd)
    message.linear = 0
    message.nonlinear = 0
    if mode == "rcm":
        message.control_bits = 132
        message.nonlinear = [robot_cmd[0], robot_cmd[1], robot_cmd[1], robot_cmd[2], robot_cmd[2]]
        message.linear = 0
    if mode == "trn":
        message.control_bits = 130
        message.linear = robot_cmd
        message.nonlinear = [0,0,0]
        lcm_cm.publish("RobotCommand", message.encode())


def encoder_data():
    """
    initilizing the subscription from the lcm
    """
    try:
        lcm_rv = lcm.LCM()
        lcm_rv.subscribe("RobotStatus", data_subscription)
        lcm_rv.handle()

    except KeyboardInterrupt:
        pass
    
    return encoder_pose, encoder_vel , rv_mode, lin_data, nonlin_data


def _test():
    for i in range(20):
        print(i)
        data_publisher('trn', 100, [1,0,0])
        pose, vel, mode, lin, non_lin = encoder_data()
        print(pose)
        print('stoped')
        data_publisher('trn',100, [0,0,0])


if __name__ == "__main__":
    _test()