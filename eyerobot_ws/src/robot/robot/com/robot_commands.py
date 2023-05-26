import lgpc.core.robot.lcm_ros_wrapper as lrw
import rclpy
import numpy as np
import math

def stop_command():
    lrw.data_publisher('stop', [0,0,0], 0)           


######################################## TRANSLATIONAL ########################################
def z_trans(robot_pose, direction = 1, dist=100, robot_init = [100000 * i for i in [1,1,1,1,1]], stop_acc = 500, speed = 10):
    """
    translational movement for 1 um
    robot_pose : coming from the encoder and subscriber
    dist = 10 is equal to 1 um 
    robot_init : the position of the defualt initilizing 
    stop accuarcy : is the difference to the target 
    stop_acc / 10 = real_accuacy in um
    speed = 100 means 1 mm per second
    retrun bool
    false = the movement is not done
    true = the movement is done
    """ 
    try:
        if direction == 1 : 
            lrw.data_publisher('trn', [1,0,0], speed = speed)
        if direction == -1 :
            lrw.data_publisher('trn', [-1,0,0], speed = speed)  
        return False 
    except KeyboardInterrupt:
        stop_command()
        return True

def y_trans(robot_pose, direction = 1, dist=100, robot_init = [100000 * i for i in [1,1,1,1,1]], stop_acc = 500, speed = 10):
    """
    translational movement for 1 um
    robot_pose : coming from the encoder and subscriber
    dist = 10 is equal to 1 um 
    robot_init : the position of the defualt initilizing 
    stop accuarcy : is the difference to the target 
    stop_acc / 10 = real_accuacy in um
    speed = 100 means 1 mm per second
    retrun bool
    false = the movement is not done
    true = the movement is done
    """ 
    try:
        if direction == 1 : 
            lrw.data_publisher('trn', [0,1,0], speed = speed)
        if direction == -1 :
            lrw.data_publisher('trn', [0,-1,0], speed = speed)
        return False 
    except KeyboardInterrupt:
        stop_command()
        return True


def x_trans(robot_pose, direction = 1, dist=100, robot_init = [100000 * i for i in [1,1,1,1,1]], stop_acc = 500, speed = 10):
    """
    translational movement for 1 um
    robot_pose : coming from the encoder and subscriber
    dist = 10 is equal to 1 um 
    robot_init : the position of the defualt initilizing 
    stop accuarcy : is the difference to the target 
    stop_acc / 10 = real_accuacy in um
    speed = 100 means 1 mm per second
    retrun bool
    false = the movement is not done
    true = the movement is done
    """ 
    try:
        if direction == 1 : 
            lrw.data_publisher('trn', [0,0,1], speed = speed)
        if direction == -1 :
            lrw.data_publisher('trn', [0,0,-1], speed = speed)
        print("Command sent")   
        return False 
    except KeyboardInterrupt:
        stop_command()
        return True



######################################## RCM MOVEMENT #################################################
def target_calculator(xz_deg= 0, yz_deg= 0):
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
        targetpos[2] = 100000 - d3 * 10000.0
        targetpos[1] = targetpos[2] - DISTANCE_SLIDE * np.tan(yz_deg)
        targetpos[4] = 100000 - d1 * 10000.0
        targetpos[3] = targetpos[4] + DISTANCE_SLIDE * np.tan(xz_deg)
        return targetpos, d5, d3, d1



def rcm(robot_pose, deg_yz, deg_xz, robot_init = [100000 * i for i in [1,1,1,1,1]], stop_acc = 500, speed_xz = 10, speed_yz = 10):
    diff = [0, 0, 0, 0, 0]
    
    if deg_xz < 0:
        speed_xz = -1 * speed_xz  
    if deg_yz > 0:
        speed_xz = -1 * speed_yz  
    
    pose_target, *other = target_calculator(deg_xz, deg_yz)
    print(pose_target)
    print(robot_pose)
    diff = abs(np.subtract(robot_pose, pose_target))
    rclpy.logging.get_logger("data").info(str(diff))

   #  diff[0] > stop_acc and diff[1] > stop_acc and diff[2] > stop_acc and diff[3] > stop_acc and diff[4] > stop_acc:
        #    print("1")
        #   lrw.data_publisher("rcm", [0, speed_yz, speed_xz])
    if diff[0] > stop_acc and diff[1] > stop_acc and diff[2] > stop_acc :
        lrw.data_publisher("rcm", [0, speed_yz, 0], speed=10)
        print("2")
    elif diff[0] > stop_acc and diff[3] > stop_acc and diff[4] > stop_acc :
        lrw.data_publisher("rcm", [0, 0, speed_xz], speed=10)
        print("3")
                
    if diff[0] < stop_acc and diff[1] < stop_acc and diff[2] < stop_acc and diff[3] < stop_acc and diff[4] < stop_acc:
        return True


######################################## INIT MOVEMEMENT ##############################################
def z_init(robot_pose, robot_target = [100000 * i for i in [1,1,1,1,1]], stop_acc = 100, speed = 50):
    
    if abs(robot_pose[0] - robot_target[0]) > stop_acc :
        if robot_pose[0] - robot_target[0] > 0:
                speed = -1 * speed
        lrw.data_publisher('trn', [1,0,0], speed= speed)
        return False
    else:
        stop_command()
        # rclpy.logging.get_logger("Stop Command").info("Y is initilized!")
        return True

def y_init(robot_pose, robot_target = [100000 * i for i in [1,1,1,1,1]], stop_acc = 100, speed = 50):
    
     
    if abs(robot_pose[0] - robot_target[0]) > stop_acc :
        if robot_pose[0] - robot_target[0] > 0:
                speed = -1 * speed
        lrw.data_publisher('trn', [1,0,0], speed= speed)
        return False
    else:
        stop_command()
        rclpy.logging.get_logger("Stop Command").info("Y is initilized!")
        return True
