#! usr/bin/env python3
from symbol import subscript
import usb.core
import time
from cgi import parse_multipart
from nis import match
from operator import is_
from tokenize import Double
from turtle import position
import math
import time
import sys
import rclpy 
from rclpy.node import Node
from robot_interface.msg import RobotCommand
from robot_interface.msg import RobotJoystick


class InputDeviceNode(Node):
    def __init__(self):
        super().__init__("Input_device_node")
        self.get_logger().info("Joystick node has been started")
        self.counter_ = 0
        self.mode_ = 'trn'
        # self.device, self.address = self.input_setup()
        self.dev, self.addr = self.joystick_setup()
        self.get_logger().info(f"device = {self.dev}, address is : {self.addr}")
        self.usb_input_pub = self.create_publisher(RobotJoystick, '/input_signal', 10)
        self.input_signal_read_timer = self.create_timer(0.01, self.joystick_reader)



    def joystick_setup(self):
        ### setting up the joystick
        dev = usb.core.find(idVendor=0x068e, idProduct=0x010c) ## represent the joystick, find the detail by using &lsusb and then &lsusb -D /dev/bus/usb/ <bus-number> / < device-number>
        ep = dev[0].interfaces()[0].endpoints()[0] ## read from the first device dev[0] interface endpoints
        i=dev[0].interfaces()[0].bInterfaceNumber ## we have descriptor 
        dev.reset()
        if dev is None:
            raise ValueError('device not found')
            sys.exit(1)
        else:
            print("Dev`ice Found")

        if dev.is_kernel_driver_active(i): ## if currently sth is listening to device we detach it.  
            try:
                dev.detach_kernel_driver(i) ## stop and detach to it
            except usb.core.USBError as e:
                sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))

        dev.set_configuration() ## start the device up
        eaddr = ep.bEndpointAddress ## just set the endpoint address 
        return dev, eaddr

    
    def joystick_signal(self):
        js = self.dev.read(self.addr, 100)
        return js
    

    def mode_selector(self, js):
        if js[6] == 1:
                print("mode_changed")
                self.mode_ = 'trn'
        if js[6] == 2:
            self.mode_ = 'rcm'
        return self.mode_

    def movement_handler(self, js, mode):
        if js[7] == 4:
            movement_code = 130.0
            movement_name = 'Z_T'
            return movement_code, movement_name 
        if js[7] == 8:
            movement_code = -130.0
            movement_name = 'Z_D'
            return movement_code, movement_name 
        if mode == 'trn':
            # movement_code = 130.2
            # movement_name = 'X_L'
            # return movement_code, movement_name 
            if js[0] == 0 and js[1] == 0:
                #print("Mode >> TRS || Dir >> X_Left   ", end='\r')
                movement_code = 130.2
                movement_name = 'X_L'
                return movement_code, movement_name 
            if js[0] == 255 and js[1] == 3:
                #print("Mode >> TRS || Dir >> X_right  ", end='\r')
                movement_code = -130.2
                movement_name = 'X_R'
                return movement_code, movement_name 
                
            
            if js[2] == 0 and js[3] == 0:
                #print("Mode >> TRS || Dir >> Y_Top   ", end='\r')
                movement_code = 130.1
                movement_name = 'Y_U'
                return movement_code, movement_name 

            if js[2] == 255 and js[3] == 3 :
                #print("Mode >> TRS || Dir >> Y_Down  ", end='\r')
                movement_code = -130.1
                movement_name = 'Y_D'
                return movement_code, movement_name 

            else: 
                movement_code = 0.0
                movement_name = 'stop'
                return movement_code, movement_name 

        if mode == 'rcm':
            if js[0] == 0 and js[1] == 0:
                movement_code = 132.0
                movement_name = 'XZ_L'
                return movement_code, movement_name 
            if js[0] == 255 and js[1] == 3:
                movement_code = -132.0
                movement_name = 'XZ_R'
                return movement_code, movement_name 
            if js[2] == 0 and js[3] == 0:
                movement_code = 132.1
                movement_name = 'XY_T'
                return movement_code, movement_name 
            if js[2] == 255 and js[3] == 3:
                movement_code = -132.1
                movement_name = 'XY_D'
                return movement_code, movement_name 
            else: 
                movement_code = 0.0
                movement_name = 'stop'
                return movement_code, movement_name 
                    
    def joystick_reader(self):
        self.counter_ +=1 
        command = RobotJoystick()
        ## signal array
        js = self.joystick_signal()
        self.mode_ = self.mode_selector(js)
        # TODO: make the speed dynamic
        command.speed = 50
        try:
            command.mode , command.mode_name = self.movement_handler(js, self.mode_)
            self.get_logger().info(f' {self.mode_} -- {command.axis}-{command.mode_name}-{js[7]}-{js[3]}')
            self.usb_input_pub.publish(command)
        except Exception as e:
            self.get_logger().error(e)

        self.usb_input_pub.publish(command)

def main(args = None):
    rclpy.init(args=args)
    node = InputDeviceNode()
    
    try:
        rclpy.logging.get_logger("Quitting").info("Done")
        rclpy.spin(node=node)
        
        pass
    except Exception as e:
        rclpy.logging.get_logger("Quitting").info(str(e))
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
'''
    
def loading_func():
    print('Mode is changing, Please Wait!')
    time.sleep(5)
    for i in range (10):
        print(f"{i/10*100:.1f} %", end="\r")
        time.sleep(0.1)


def trans_movement(input, act_speed=100):
    message.nonlinear[0] = 0 #movementSpeed 
    message.nonlinear[1] = 0 #movementSpeed
    message.nonlinear[2] = 0 #movementSpeed 
    if input[0] == 0 and input[1] == 0:
        print("Mode >> TRS || Dir >> X_Left   ", end='\r')
        message.control_bits = 130
        message.linear[0] = 0 #movementSpeed 
        message.linear[1] = 0 #movementSpeed
        message.linear[2] = act_speed
    if input[0] == 255 and input[1] == 3:
        print("Mode >> TRS || Dir >> X_right  ", end='\r')
        message.control_bits = 130
        message.linear[0] = 0 #movementSpeed 
        message.linear[1] = 0 #movementSpeed
        message.linear[2] =  act_speed * -1
    
    if input[2] == 0 and input[3] == 0:
        print("Mode >> TRS || Dir >> Y_Top   ", end='\r')
        message.control_bits = 130
        message.linear[0] = 0 #movementSpeed 
        message.linear[1] = act_speed #movementSpeed
        message.linear[2] = 0

    if input[2] == 255 and input[3] == 3 :
        print("Mode >> TRS || Dir >> Y_Down  ", end='\r')
        message.control_bits = 130
        message.linear[0] = 0 #movementSpeed 
        message.linear[1] = act_speed * -1 #movementSpeed
        message.linear[2] =  0
    
    lcm_cm.publish("RobotCommand", message.encode())

    

def rcm_movement(input , act_speed= 100):
    message.linear[0] = 0  
    message.linear[1] = 0 
    message.linear[2] = 0
    if input[0] == 0 and input[1] == 0:
        print("Mode >> RCM || Dir >> XZ_Left", end='\r')
        message.control_bits = 132
        message.nonlinear[0] = 0 #movementSpeed 
        message.nonlinear[1] = act_speed * -1 #movementSpeed
        message.nonlinear[2] = 0
    
    if input[0] == 255 and input[1] == 3 :
        print("Mode >> RCM || Dir >> XZ_right", end='\r')
        message.control_bits = 132
        message.nonlinear[0] = 0 #movementSpeed 
        message.nonlinear[1] = act_speed  #movementSpeed
        message.nonlinear[2] = 0
  
    if input[2] == 0 and input[3] == 0:
        print("Mode >> RCM || Dir >> XY_top", end='\r')
        message.control_bits = 132
        message.nonlinear[0] = 0 #movementSpeed 
        message.nonlinear[1] = 0 #movementSpeed
        message.nonlinear[2] =  act_speed 
    
        
    if input[2] == 255 and input[3] == 3:
        print("Mode >> RCM || Dir >> XY_Down", end='\r')
        message.control_bits = 132
        message.nonlinear[0] = 0 #movementSpeed 
        message.nonlinear[1] = 0 #movementSpeed
        message.nonlinear[2] =  act_speed * -1
    lcm_cm.publish("RobotCommand", message.encode())



    

def z_movement(input, mode, act_speed = 50):
    #print(f'                           ||{input}', end='\r')
    if input[7] == 4:
        if mode: 
            print('Mode >> TRS || Dir >> Z-Top     ', end='\r')
        else:
            print('Mode >> RCM || Dir >> Z-Top     ', end='\r') 
        
        message.control_bits = 130
        message.linear[0] = act_speed
        message.linear[1] = 0 #movementSpeed
        message.linear[2] =  0
        lcm_cm.publish("RobotCommand", message.encode())
        
    if input[7] == 8:
        if mode: 
            print('Mode >> TRS || Dir >> Z-Down    ', end='\r')
        else:
            print('Mode >> RCM || Dir >> Z-Down    ', end='\r') 
        
        message.control_bits = 130
        message.linear[0] = act_speed * -1
        message.linear[1] = 0 #movementSpeed
        message.linear[2] =  0
        lcm_cm.publish("RobotCommand", message.encode())
    
    if input[7] != 4 and input[7] != 8:
        if mode: 
            print('Mode >> TRS || Dir >>                    ', end='\r')
        else:
            print('Mode >> RCM || Dir >>                    ', end='\r')
        message.control_bits = 0
        message.linear[0] = 0 #movementSpeed 
        message.linear[1] = 0 #movementSpeed
        message.linear[2] =  0
        message.nonlinear[0] = 0 #movementSpeed 
        message.nonlinear[1] = 0 #movementSpeed
        message.nonlinear[2] = 0 #movementSpeed
        lcm_cm.publish("RobotCommand", message.encode())



def stop_command():
        message.control_bits = 0
        message.linear[0] = 0 #movementSpeed 
        message.linear[1] = 0 #movementSpeed
        message.linear[2] =  0
        message.nonlinear[0] = 0 #movementSpeed 
        message.nonlinear[1] = 0 #movementSpeed
        message.nonlinear[2] = 0 #movementSpeed
        lcm_cm.publish("RobotCommand", message.encode())


def mode_displayer(mode):
    if mode:
        print(f"mode >> Translational", end='\r')
    else:
        print(f"mode >> RCM", end='\r')

tran_mod = True # 0 > Tr 1 > RCM
while True:

    
    js= joystick_decoder()
    r = dev.read(eaddr, 100)
    if r[6] == 1:
        print(f'Mode is changing to RCM, Please Wait!                           ', end='\r')
        time.sleep(2)
        # for i in range (10):
        #     print(f"Please Wait!! {i/10*100:.1f} %", end="\r")
        # time.sleep(0.1)
        tran_mod = False
        

    if r[6] == 2:
        print(f'Mode is changing to Translational, Please Wait!                           ', end='\r')
        time.sleep(2)
        # for i in range (10):
        #     print(f"{i/10*100:.1f} %", end="\r")
        # time.sleep(0.5)
        tran_mod = True
        

        
        

        
    js = joystick_decoder()
    z_movement(js, tran_mod)
    


    if tran_mod:
        trans_movement(js)
    elif not tran_mod:
        rcm_movement(js)
    else:
        stop_command()
    
    # if is_z_limit :
    #     message.control_bits = 0
    #     message.linear[0] = 0
    #     lcm_cm.publish("RobotCommand", message.encode())
    

    '''
    






    