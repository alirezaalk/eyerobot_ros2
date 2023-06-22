from symbol import subscript
import usb.core
import time
from cgi import parse_multipart
from nis import match
from operator import is_
from tokenize import Double
from turtle import position
import lcm
import math
import time
from RobotMessage import RobotMessage 
import sys


### setting up LCM
lcm_rv = lcm.LCM()  #  receive status
lcm_cm = lcm.LCM()  #  send command 
message = RobotMessage()
## Setting up the target and encoders data
target_A = [ 100000, 110000, 110000, 100000, 10000]

encoder0 = []
encoder1 = []
encoder2 = []
encoder3 = []
encoder4 = []

encoder0 = []
encoder1 = []
encoder2 = []
encoder3 = []
encoder4 = []
command0 = []
command1 = []
command2 = []

### break motion for the start of the movement
message.control_bits = 0
message.linear[0] = 0
message.linear[1] = 0
message.linear[2] = 0
message.nonlinear[0] = 0
message.nonlinear[1] = 0
message.nonlinear[2] = 0

### setting up the joystick
dev = usb.core.find(idVendor=0x068e, idProduct=0x010c) ## represent the joystick, find the detail by using &lsusb and then &lsusb -D /dev/bus/usb/ <bus-number> / < device-number>
ep = dev[0].interfaces()[0].endpoints()[0] ## read from the first device dev[0] interface endpoints
i=dev[0].interfaces()[0].bInterfaceNumber ## we have descriptor 
dev.reset()
if dev is None:
    raise ValueError('device not found')
    sys.exit(1)
else:
    print("Device Found")

if dev.is_kernel_driver_active(i): ## if currently sth is listening to device we detach it.  
    try:
        dev.detach_kernel_driver(i) ## stop and detach to it
    except usb.core.USBError as e:
        sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))

dev.set_configuration() ## start the device up
eaddr = ep.bEndpointAddress ## just set the endpoint address 

axis = 0
def decode(channel, data):
    global is_z_limit
    msg = RobotMessage.decode(data)
    

def joystick_decoder():
    js = dev.read(eaddr, 100)
    return js


def joystick_mode():
    number = dev.read(eaddr, 100)[6]
    if mode == 1:
        print("mode_changed")
        if number == 0 :
            mode = 1
        else:
            mode = 0
        return mode
    
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
    

    
    






    