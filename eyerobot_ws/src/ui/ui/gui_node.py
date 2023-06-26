import sys
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QAction, QStyle, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import numpy as np
# from ui_handler import UIHandler
from PyQt5 import QtWidgets
import rclpy
from rclpy.node import Node
from ui.configs.ui_config import UiConfig
from PyQt5 import uic
from PyQt5 import QtWidgets
from sensor_msgs.msg import Image
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from cv_bridge import CvBridge
import cv2
import time
from ui.packages.splash_screen import SplashScreen
from robot_interface.msg import RobotPose
from robot_interface.msg import RobotCommand
from robot_interface.msg import RobotFeedback
from std_msgs.msg import UInt16
import robot.robot_excutor as rcomp
from PyQt5.QtGui import QMouseEvent
# from robot_interface.srv import RobotCom
### Robot init import
#import robot.excutor as re


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # ROS2 init
        rclpy.init(args=None)
        self.node = Node('gui_node')
        self.node.get_logger().info("QT main window node has been started")
        # rclpy.spin(self.node)
        
        # init cvbridge to be able subscribing image data from publisher
        self.bridge = CvBridge()
        
        # Build splash screen and UI
        #splash_screen = SplashScreen()
        self.ui = uic.loadUi(UiConfig().UI_DIR + 'main_ui.ui')
        self.ui.log_console.append("Medical Autonomy and Precision Surgery Laboratory\n")
        # add windows icon to the the app
        # self.setWindowIcon(QIcon(self.icon_path))
        
        # Connect UI signals

        ## RGBD Camera Button
        self.d445_topic_name = "/d445_images"
        self.ui.d445_start_but.clicked.connect(self.start_camera_subscription)
        self.ui.d445_stop_but.clicked.connect(self.stop_camera_subscription)
        


        # Basler Camera Top 
        self.cam_top_topic_name = "/cam_top"
        self.ui.start_camera_top.clicked.connect(self.cam_top_start_sub)



        ## Monitor the data
        self.pose_sub_topic= '/encoder_gui'
        self.encoder_sub = self.node.create_subscription(
            RobotPose,
            self.pose_sub_topic,
            self.encoder_gui,
            10)
        self.encoder_sub = self.node.create_subscription(
            RobotPose,
            '/move_status',
            self.log_encoder,
            10)
        self.ui.clear_log_but.clicked.connect(self.clear_encoder_log)
        
        ### Robot command button 
        self.ui.robot_init_but.clicked.connect(self.robot_init_cmd)
        self.ui.robot_calib_but.clicked.connect(self.robot_calibration)

        self.cmd_gui_pub = self.node.create_publisher(
            RobotCommand,
            '/cmd_pose',
            10)

        self.feedback_slam_gui_sub = self.node.create_subscription(
            RobotFeedback,
            '/slam_feedback',
            self.feedback_slam_gui,
            10)
        self.feedback_value = [0.0,0.0,0.0]
        self.feedback_result = ''
        self.init_done = False
        self.deg_xz = 2.0
        self.deg_yz = 2.0
        ## TODO if case adding the Rosservice 
        ### Service 
        
        # self.robot_init_client = self.node.create_client(
        #         RobotCom, 
        #         "robot_command")
        # self.req = RobotCom.Request()




        ## TODO add arrow button
        ## Arrow buttons
        self.input_signal_pub = self.node.create_publisher(
            RobotCommand, 
            '/movemnet_api',
            10)
        
        self.ui.up_but.clicked.connect(self.emit_signal_up)
        self.ui.down_but.clicked.connect(self.emit_signal_down)
        self.ui.control_up.mousePressEvent = self.emit_signal_y_top
        self.ui.control_down.mousePressEvent = self.emit_signal_y_down
        self.ui.control_left.mousePressEvent = self.emit_signal_x_left
        self.ui.control_right.mousePressEvent = self.emit_signal_x_right
        
        ## Set the ui elements in start mode
        self.ui.progressBar.setValue(0)
    
    
    ########################## Display contained UI ##############################
    def show(self):
        self.ui.show()

    
    def update_progressBar(self, percent):
        self.ui.progressBar.setValue(percent)

    
    def update_console_encoder_2(self, text):
        # log_text = "Calibration Is Pressed"
        self.ui.log_encoder_2.append(text)
    ##### 
    def show_frame(self, target_label: QLabel, image):
        # # scaling the image while showing in the ui
        scale_factor = 0.5
        target_label.setPixmap(convert_cv_qt(image))
        target_label.setMinimumHeight(image.shape[0] * scale_factor * 2.3)
        target_label.setMinimumWidth(image.shape[1] * scale_factor)
        QApplication.processEvents()
        # time.sleep(0.1)
        if False: 
            cv2.imshow('frame', image)
            cv2.waitKey(1)

    #################################### Main Page ###########################
    def emit_signal_up(self):
        
        cmd = RobotCommand()
        self.ui.log_console.clear()
        self.ui.log_console.append("Z-Up")
        cmd.name = 'w_target'
        cmd.speed = 100
        cmd.command = 130.0
        self.input_signal_pub.publish(cmd)
    
    def emit_signal_down(self):
        cmd = RobotCommand()
        self.ui.log_console.clear()
        self.ui.log_console.append("Z-Down")
        cmd.name = 'w_target'
        cmd.speed = 100
        cmd.command = -130.0
        self.input_signal_pub.publish(cmd)

    def emit_signal_y_top(self,  mouse_event: QMouseEvent):
        cmd = RobotCommand()
        self.ui.log_console.clear()
        cmd.name = 'w_target'
        cmd.speed = 100
        
        if self.ui.checkBox_rcm_trn.isChecked() == True:
            self.ui.log_console.append("XY-Up")
            cmd.command = 132.0
        if self.ui.checkBox_rcm_trn.isChecked() == False:
            cmd.command = 130.1
            self.ui.log_console.append("Y-Up")
        self.input_signal_pub.publish(cmd)
    
    def emit_signal_y_down(self,  mouse_event: QMouseEvent):
        cmd = RobotCommand()
        self.ui.log_console.clear()
        cmd.name = 'w_target'
        cmd.speed = 100
        
        if self.ui.checkBox_rcm_trn.isChecked() == True:
            self.ui.log_console.append("XY-Down")
            cmd.command = -132.0
        if self.ui.checkBox_rcm_trn.isChecked() == False:
            cmd.command = -130.1
            self.ui.log_console.append("Y-Down")
        self.input_signal_pub.publish(cmd)

    def emit_signal_x_left(self,  mouse_event: QMouseEvent):
        cmd = RobotCommand()
        self.ui.log_console.clear()
        cmd.name = 'w_target'
        cmd.speed = 100
        
        if self.ui.checkBox_rcm_trn.isChecked() == True:
            self.ui.log_console.append("XZ-Left")
            cmd.command = 132.1
        if self.ui.checkBox_rcm_trn.isChecked() == False:
            cmd.command = 130.2
            self.ui.log_console.append("X-Left")
        self.input_signal_pub.publish(cmd)
    
    def emit_signal_x_right(self,  mouse_event: QMouseEvent):
        cmd = RobotCommand()
        self.ui.log_console.clear()
        
        cmd.name = 'w_target'
        cmd.speed = 100
        
        if self.ui.checkBox_rcm_trn.isChecked() == True:
            self.ui.log_console.append("XZ-Right")
            cmd.command = -132.1
        if self.ui.checkBox_rcm_trn.isChecked() == False:
            cmd.command = -130.2
            self.ui.log_console.append("X-right")
        self.input_signal_pub.publish(cmd)

   

        
    def robot_init_cmd(self):
        self.ui.log_console.append("init is pressed")
        self.init_timer = self.node.create_timer(0.01, self.slam_cmd_init)
        self.init_done = False
        self.ui.log_encoder_2.clear()
        log_text = "Initialization Is Pressed"
        self.ui.log_encoder_2.append(log_text)
        self.update_progressBar(0)


    def robot_calibration(self):
        cmd = RobotCommand()
        cmd.name = 'robot_calib_set_target'
        self.feedback_value == [0.0,0.0,0.0]
        self.deg_xz = 5.0
        self.deg_yz = 5.0
        self.rcm_target_pose = self.target_calculator(self.robot_pose, self.deg_xz, self.deg_yz)
        print('calculated_pose: ', self.rcm_target_pose)
        self.ui.log_console.append("Calibration Button is pressed")
        self.calibration_timer = self.node.create_timer(0.01, self.slam_calibration_cmd)
        self.calib_done = False
        self.update_console_encoder_2("Calibration Is Pressed")
        self.update_progressBar(1)
        # print('calibration is pressed')
        

    def feedback_slam_gui(self, feedback:RobotFeedback):
        """
        This function is responsible for subscribing the feedback in GUI coming from SLAM
        3 important parameters is 
        feedback name : returns the name of the current mission
        feedback mode : return the mode and axis of the motion
        feedback_key : return the current status of the motion
            111 : ongoing
            100 : done
            200 : failed
        feedback_value = [
        0- feedback_name
        1- feedback_mode
        2- feedback_key
        ]
        """
        feedback_name = feedback.name
        self.feedback_result = feedback.result
        self.feedback_mode = feedback.key.x
        self.feedback_key = feedback.key.y
        self.feedback_value = [feedback_name, feedback.key.x, feedback.key.y]
        ## Update the log_encoders 
        self.ui.log_encoder_2.clear()
        self.ui.log_encoder_2.append(f'Feedback: {str(self.feedback_value)}')
        self.ui.log_status.clear()
        self.ui.log_status.append(f'Robot Status: {self.feedback_value[0]}')


    def slam_calibration_cmd(self):
        ### set the command
        cmd = RobotCommand()
        """
        The Calibration Process:
        To start the process: Either we have 
        ['Standby', 0.0, 0.0] feedback from the slam 
        or 
        [0.0, 0.0, 0.0] after starting the progress
        after that we need to calculate the first RCM movement with the posstive degree
        then set the target point and move in yz and xz -- the flag is robot_calib
        when the first movement is done we need to calculate the new target pose with the current robot_pose for returning and negative degrees
        then we set the targetpoint and move in yz and xz --- the flag is robot_calib_r
        then send the Calibration done signal to slam and slam put the robot in the standby and make the timer off
        """
        ## Start the movement in XZ
        if self.feedback_value == [0.0,0.0,0.0] or self.feedback_value == ['Standby', 0.0, 0.0 ]:
            cmd.name = 'robot_calib'
            cmd.mode = 132.0 
            cmd.target0 = self.rcm_target_pose[0]
            cmd.target1 = self.rcm_target_pose[1]
            cmd.target2 = self.rcm_target_pose[2]
            cmd.target3 = self.rcm_target_pose[3]
            cmd.target4 = self.rcm_target_pose[4]
            cmd.coordinate.orientation.x = self.deg_xz
            cmd.coordinate.orientation.y = self.deg_yz
            self.cmd_gui_pub.publish(cmd)
            self.update_progressBar(3)

        ## Movement is XZ is running 
        if self.feedback_value == ['robot_calib',132.0,111.0] or self.feedback_value == ['robot_calib_r',132.0,111.0]:
            cmd.name = self.feedback_value[0]
            cmd.mode = 132.0 
            cmd.target0 = self.rcm_target_pose[0]
            cmd.target1 = self.rcm_target_pose[1]
            cmd.target2 = self.rcm_target_pose[2]
            cmd.target3 = self.rcm_target_pose[3]
            cmd.target4 = self.rcm_target_pose[4]
            cmd.coordinate.orientation.x = self.deg_xz
            cmd.coordinate.orientation.y = self.deg_yz
            self.cmd_gui_pub.publish(cmd)
            if cmd.name == 'robot_calib':
                self.update_progressBar(15)
            if cmd.name == 'robot_calib_r':
                self.update_progressBar(65)
        
        ## XZ Movement is Done
        if self.feedback_value == ['robot_calib',132.0,100.0] or self.feedback_value == ['robot_calib_r',132.0,100.0] : 
            cmd.name = self.feedback_value[0]
            cmd.mode = 132.1 
            cmd.target0 = self.rcm_target_pose[0]
            cmd.target1 = self.rcm_target_pose[1]
            cmd.target2 = self.rcm_target_pose[2]
            cmd.target3 = self.rcm_target_pose[3]
            cmd.target4 = self.rcm_target_pose[4]
            cmd.coordinate.orientation.x = self.deg_xz
            cmd.coordinate.orientation.y = self.deg_yz
            self.cmd_gui_pub.publish(cmd)
            if cmd.name == 'robot_calib':
                self.update_progressBar(25)
            if cmd.name == 'robot_calib_r':
                self.update_progressBar(74)
        if self.feedback_value == ['robot_calib',132.1,111.0] or self.feedback_value == ['robot_calib_r',132.1,111.0]:
            cmd.name = self.feedback_value[0]
            cmd.mode = 132.1 
            cmd.target0 = self.rcm_target_pose[0]
            cmd.target1 = self.rcm_target_pose[1]
            cmd.target2 = self.rcm_target_pose[2]
            cmd.target3 = self.rcm_target_pose[3]
            cmd.target4 = self.rcm_target_pose[4]
            cmd.coordinate.orientation.x = self.deg_xz
            cmd.coordinate.orientation.y = self.deg_yz
            self.cmd_gui_pub.publish(cmd)
            if cmd.name == 'robot_calib':
                self.update_progressBar(34)
            if cmd.name == 'robot_calib_r':
                self.update_progressBar(94)
        
        if self.feedback_value == ['robot_calib',132.1,100.0]:
            self.deg_xz = -5.0
            self.deg_yz = -5.0
            self.rcm_target_pose = self.target_calculator(self.robot_pose, self.deg_xz, self.deg_yz)
            cmd.name = 'robot_calib_r'
            cmd.mode = 132.0 
            cmd.target0 = self.rcm_target_pose[0]
            cmd.target1 = self.rcm_target_pose[1]
            cmd.target2 = self.rcm_target_pose[2]
            cmd.target3 = self.rcm_target_pose[3]
            cmd.target4 = self.rcm_target_pose[4]
            cmd.coordinate.orientation.x = self.deg_xz
            cmd.coordinate.orientation.y = self.deg_yz
            self.cmd_gui_pub.publish(cmd)
            self.update_progressBar(55)
        ## the robot_calib_r is done means the robot returns to the original position
        if self.feedback_value == ['robot_calib_r',132.1,100.0]:
            cmd.name = 'robot_calib_r'
            self.init_done = True
            cmd.mode = 0.0
            self.cmd_gui_pub.publish(cmd)
            # print('Cancel')
            # self.feedback_value = [0.0,0.0,0.0]
            self.calibration_timer.cancel()
            self.update_progressBar(100)


    def slam_cmd_init(self):
        """
        This function activates based on the timer_robot_init 
        Get the data from the slam and send out the init command
        Init parameters can be set with the UI 
        TODO add the init parameters to the Project config
        """
        ### set the command
        cmd = RobotCommand()
        cmd.speed = 50
        cmd.stop_limit = 1000
        cmd.coordinate.position.x = 100000.0
        cmd.coordinate.position.y = 100000.0
        cmd.coordinate.position.z = 100000.0
        cmd.coordinate.orientation.x = 0.0
        cmd.coordinate.orientation.y = 0.0
        cmd.coordinate.orientation.z = 0.0
        
        ## first step of the init
        self.ui.log_encoder_2.clear()
        if self.feedback_value == [0,0,0] or ['Standby', 0.0, 0.0] :
            cmd.name = 'robot_init'
            cmd.mode = 130.0  
            self.cmd_gui_pub.publish(cmd)
            self.update_progressBar(5)
        ## the robot is in init_z
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.0 and self.feedback_value[2] == 111.0:
            cmd.name = 'robot_init'
            cmd.mode = 130.0  
            self.cmd_gui_pub.publish(cmd) 
            log_text = "Initialization X-Axis"
            self.ui.log_encoder_2.append(log_text)
            self.update_progressBar(20)  
        ## init_z is done and send a command to start init_y
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.0 and self.feedback_value[2] == 100.0 :
            cmd.name = 'robot_init'
            cmd.mode = 130.1
            self.cmd_gui_pub.publish(cmd)
            log_text = "X-Axis is Done-Initialization Y-Axis Starts"
            self.ui.log_encoder_2.append(log_text)
            self.update_progressBar(33)
        ## robot is in init_y 
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.1 and self.feedback_value[2] == 111.0:
            cmd.name = 'robot_init'
            cmd.mode = 130.1
            self.cmd_gui_pub.publish(cmd)
            log_text = "Initialization Y-Axis"
            self.ui.log_encoder_2.append(log_text)
            self.update_progressBar(55)
            
        ## init_y is done and send 130.2 to start init_x
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.1 and self.feedback_value[2] == 100.0:
            cmd.name = 'robot_init'
            cmd.mode = 130.2
            self.cmd_gui_pub.publish(cmd)
            log_text = "Y-Axis is Done- Initialization Z-Axis Starts"
            self.ui.log_encoder_2.append(log_text)
            self.update_progressBar(66)
        ## init_x is ongoing
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.2 and self.feedback_value[2] == 111.0:
            cmd.name = 'robot_init'
            cmd.mode = 130.2
            self.cmd_gui_pub.publish(cmd)
            log_text = "Initialization Is Done"
            self.ui.log_encoder_2.append(log_text)
            self.update_progressBar(85)
        ## init_x is done 
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.2 and self.feedback_value[2] == 100.0:
            print('DONE!')
            self.init_done = True
            cmd.name = 'robot_init'
            cmd.mode = 0.0
            self.cmd_gui_pub.publish(cmd)
            self.init_timer.cancel()
            log_text = "Initialization Is Done-Timer Is OFF"
            self.ui.log_encoder_2.append(log_text)
            self.update_progressBar(100)
        if self.init_done:
            print('current result: ', self.feedback_value)
            self.init_timer.cancel()
            self.cmd_gui_pub.publish(cmd)
            

    def target_calculator(self, robot_pose, xz_deg= 0, yz_deg= 0):
        xz_deg = xz_deg/-180*np.pi
        yz_deg = yz_deg/-180*np.pi
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
        targetpos[2] =  robot_pose[2]- d3 * 10000.0
        targetpos[1] = targetpos[2] - DISTANCE_SLIDE * np.tan(yz_deg)
        targetpos[4] =  robot_pose[4] - d1 * 10000.0
        targetpos[3] = targetpos[4] + DISTANCE_SLIDE * np.tan(xz_deg)
        return targetpos# , d5, d3, d1

    ########## SERVICE
    # def robot_init(self):
    #     while not self.robot_init_client.wait_for_service(timeout_sec = 1.0):
    #         self.node.get_logger().error("Serive is not available!")
    #     self.ui.log_console.append("robot is initlizing")
    #     self.req.mode = 100.0
    #     self.req.speed = 38
    #     self.req.stop_limit = 100
    #     self.req.name = 'Init'
    #     self.req.coordinate.position.x = 100000.0
    #     self.req.coordinate.position.y = 100000.0
    #     self.req.coordinate.position.z = 100000.0
    #     self.req.coordinate.orientation.x = 100000.0
    #     self.req.coordinate.orientation.y = 100000.0
    #     self.req.coordinate.orientation.z = 0.0
    #     self.future = self.robot_init_client.call_async(self.req)
    #     print(self.future)
    
    #### Calculate the pose based on the encoder
    def pose_calculator(self, pos_array, 
                        link1 = 29.50, link2= 47.80, offset1 = 4.75, 
                        offset2 = 19.00, ltool = 62.25, d1 = 101.00, 
                        d3 = 63.01, d5 = 85.25
                        ):
        tip_pose = [0,0,0]
        d5_pos = (pos_array[0] - 100000) / 10000 + 85.25
        d3_pos = -(pos_array[2] - 100000)/10000 + 63.01
        d1_pos = -(pos_array[4] - 100000)/10000 +101    
        t2 = np.arctan((pos_array[3] - pos_array[4])/(10000*23)) 
        t4 = np.arctan(-(pos_array[1] - pos_array[2])/(10000*23)) 
        trans_pose = [d5_pos, d3_pos, d1_pos]
        rot_pose   = [t2, t4]
        self.tip_pose = [
            -1 * d5_pos * np.cos(t2) + link1 * np.sin(t2) - link2 * np.sin(t4) * np.cos(t2) - offset1 * np.cos(t2) - offset2 * np.sin(t2),
            d3_pos - d5_pos * np.sin(t4) + link2 * np.cos(t4),
            d1_pos + d5_pos * np.sin(t2) * np.cos(t4) + link1 * np.cos(t2) + link2 * np.sin(t2) * np.sin(t4) + offset1 * np.sin(t2) - offset2 * np.cos(t2) 
        ]
        return self.tip_pose
    


    def clear_encoder_log(self):
        self.ui.log_encoder.clear()

    def encoder_gui(self, pose:RobotPose):
        
        self.ui.log_encoder.clear()
        self.robot_pose = [pose.en0, pose.en1, pose.en2, pose.en3, pose.en4]
        speed = pose.speed
        name = pose.name
        tip_pose = self.pose_calculator(self.robot_pose)
        tip_pose = [round(i, 2) for i in tip_pose]
        self.ui.log_encoder.append(f"Encoders:{str(self.robot_pose)} \nTip_Pose : {str(tip_pose)}")
    
    def monitor_encoders(self):
        print("monitor data started")
        self.encoder_sub = self.node.create_subscription(
            RobotPose,
            '/encoder_data',
            self.encoder_gui,
            1)

    def log_encoder(self, pose:RobotPose):
        self.robot_pose = pose.mode
        print(self.robot_pose)
        self.ui.log_console.clear()
        self.ui.log_console.append(f"{str(self.robot_pose)}")  
    
    # live camera extraction 
    def update_pixmap_cam_top(self, image_message: Image):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(image_message, desired_encoding="passthrough")
        except:
            print("subscription faild")
        self.show_frame(self.ui.camera_top_image, cv_image)
    

    def cam_top_start_sub(self, state):
        log_string = "Microscope Camera is running\n"
        # self.ui.log_console.append("Medical Autonomy and Precision Surgery Laboratory - Robot Control UI\n")
        self.ui.log_console.append(log_string)
        print("cam top clicked")
        self.cam_top_sub = self.node.create_subscription(
            Image,
            self.cam_top_topic_name,
            self.update_pixmap_cam_top,
            1 )
        try:
            rclpy.spin(self.node)
        except KeyboardInterrupt:
            pass
    #################################### Frame Page ########################333
    # Start subscribing the d455
    def start_camera_subscription(self, state):
        log_string = "Camera is running"
        self.ui.log_console.append(log_string)
        if (True):
            try:
                # # ROS2 init
                # rclpy.init(args=None)
                # self.node = Node('gui_node')
                # self.node.get_logger().info("QT main window node has been started")
                self.sub = self.node.create_subscription(
                    Image,
                    self.d445_topic_name,
                    self.update_pixmap_realsense,
                    1,
                )

                # spin once, timeout_sec 5[s]
                timeout_sec_rclpy = 5
                timeout_init = time.time()
                # rclpy.spin(self.node)
                #rclpy.spin_once(self.node, timeout_sec=timeout_sec_rclpy)
                timeout_end = time.time()
                ros_connect_time = timeout_end - timeout_init

                ## TODO add labels for error handling
                # Error Handle for rclpy timeout
                if ros_connect_time >= timeout_sec_rclpy:
                    self.ui.label_ros2_state_float.setText("Couldn't Connect")
                    self.ui.label_ros2_state_float.setStyleSheet(
                        "color: rgb(255,255,255);"
                        "background-color: rgb(255,0,51);"
                        "border-radius:5px;"
                    )
                    ## show the sign to stop the subscription
                    raise SystemExit
                else:
                    self.ui.label_ros2_state_float.setText("Connected")
                    self.ui.label_ros2_state_float.setStyleSheet(
                        "color: rgb(255,255,255);"
                        "background-color: rgb(18,230,95);"
                        "border-radius:5px;"
                    )
            except SystemExit:
                self.node.destroy_node()
                rclpy.logging.get_logger("Quitting").info("Movement is Done!")
                rclpy.shutdown()
        else:
            self.node.destroy_node()
            rclpy.shutdown()

    def stop_camera_subscription(self):
        self.node.destroy_node()
        rclpy.logging.get_logger("Quitting").info("Movement is Done!")
        rclpy.shutdown()

    # live camera extraction 
    def update_pixmap_realsense(self, image_message: Image):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(image_message, desired_encoding="passthrough")
        except:
            print("subscription faild")
        self.node.get_logger().info("Recieved")

        self.show_frame(self.ui.d445_image, cv_image)


def convert_cv_qt(cv_image: np.ndarray):
        """Convert from an opencv image to QPixmap"""
        h, w, ch = cv_image.shape
        bytes_per_line = ch * w
        qt_image = QtGui.QImage(cv_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        return QPixmap.fromImage(qt_image)


def test_():
    MainWindow()


def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
        #app = QApplication(sys.argv)
        win = MainWindow()
        
        splash_screen = SplashScreen()
        splash_screen.show()
        app.processEvents()
        # Display splash screen while UI loads
        splash_screen.finish(win.ui)
        win.show()
        # app.exec()
        sys.exit(app.exec_())
    
    except KeyboardInterrupt:
        pass
        
if __name__ == "__main__":
    main()