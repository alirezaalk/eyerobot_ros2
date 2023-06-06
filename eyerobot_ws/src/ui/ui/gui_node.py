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
# from robot_interface.srv import RobotCom
### Robot init import
import robot.excutor as re
import robot.robot_slam_trn 

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
        self.ui.log_console.append("Medical Autonomy and Precision Surgery Laboratory - Robot Control UI\n")
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

        self.cmd_gui_pub = self.node.create_publisher(
            RobotCommand,
            '/cmd_pose',
            10)

        self.feedback_slam_gui_sub = self.node.create_subscription(
            RobotFeedback,
            '/slam_feedback',
            self.feedback_slam_gui,
            10)
        self.feedback_value = [0,0,0]
        self.feedback_result = ''
        self.init_done = False
        
        ## TODO if case adding the Rosservice 
        ### Service 
        # self.robot_init_client = self.node.create_client(
        #         RobotCom, 
        #         "robot_command")
        # self.req = RobotCom.Request()




        ## TODO add arrow button
        ## Arrow buttons
        # self.ui.control_up.mousePressEvent = self.emit_signal_up
        # self.ui.control_down.mousePressEvent = self.emit_signal_down
        # self.ui.control_left.mousePressEvent = self.emit_signal_left
        # self.ui.control_right.mousePressEvent = self.emit_signal_right
        
    
    
    ########################## Display contained UI ##############################
    def show(self):
        self.ui.show()


    ##### 
    def show_frame(self, target_label: QLabel, image ):
        # # scaling the image while showing in the ui
        scale_factor = 0.5
        target_label.setPixmap(convert_cv_qt(image))
        target_label.setMaximumHeight(image.shape[0] * scale_factor)
        target_label.setMaximumWidth(image.shape[1] * scale_factor)
        QApplication.processEvents()
        # time.sleep(0.1)
        if False: 
            cv2.imshow('frame', image)
            cv2.waitKey(1)

    #################################### Main Page ###########################
    def robot_init_cmd(self):
        self.ui.log_console.append("init is pressed")
        self.init_timer = self.node.create_timer(0.01, self.slam_cmd_init)
        self.init_done = False
        self.ui.log_encoder_2.clear()
        log_text = "Initialization Is Pressed"
        self.ui.log_encoder_2.append(log_text)
       

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
            
        ## the robot is in init_z
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.0 and self.feedback_value[2] == 111.0:
            cmd.name = 'robot_init'
            cmd.mode = 130.0  
            self.cmd_gui_pub.publish(cmd) 
            log_text = "Initialization X-Axis"
            self.ui.log_encoder_2.append(log_text)    
        ## init_z is done and send a command to start init_y
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.0 and self.feedback_value[2] == 100.0 :
            print('Z is done')
            cmd.name = 'robot_init'
            cmd.mode = 130.1
            self.cmd_gui_pub.publish(cmd)
            log_text = "X-Axis is Done-Initialization Y-Axis Starts"
            self.ui.log_encoder_2.append(log_text)
        ## robot is in init_y 
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.1 and self.feedback_value[2] == 111.0:
            print(self.feedback_result)
            cmd.name = 'robot_init'
            cmd.mode = 130.1
            self.cmd_gui_pub.publish(cmd)
            log_text = "Initialization Y-Axis"
            self.ui.log_encoder_2.append(log_text)
            
        ## init_y is done and send 130.2 to start init_x
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.1 and self.feedback_value[2] == 100.0:
            print(self.feedback_result)
            cmd.name = 'robot_init'
            cmd.mode = 130.2
            self.cmd_gui_pub.publish(cmd)
            log_text = "Y-Axis is Done- Initialization Z-Axis Starts"
            self.ui.log_encoder_2.append(log_text)
        ## init_x is ongoing
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.2 and self.feedback_value[2] == 111.0:
            print(self.feedback_result)
            cmd.name = 'robot_init'
            cmd.mode = 130.2
            self.cmd_gui_pub.publish(cmd)
            log_text = "Initialization Is Done"
            self.ui.log_encoder_2.append(log_text)
        ## init_x is done 
        if self.feedback_value[0] == 'robot_init' and abs(self.feedback_value[1]) == 130.2 and self.feedback_value[2] == 100.0:
            print(self.feedback_result)
            print('DONE!')
            self.init_done = True
            cmd.name = 'robot_init'
            cmd.mode = 0.0
            self.cmd_gui_pub.publish(cmd)
            self.init_timer.cancel()
            log_text = "Initialization Is Done-Timer Is OFF"
            self.ui.log_encoder_2.append(log_text)
        if self.init_done:
            print(self.feedback_value)
            self.init_timer.cancel()
            self.cmd_gui_pub.publish(cmd)




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
        
    
    def clear_encoder_log(self):
        self.ui.log_encoder.clear()

    def encoder_gui(self, pose:RobotPose):
        self.ui.log_encoder.clear()
        robot_pose = [pose.en0, pose.en1, pose.en2, pose.en3, pose.en4]
        speed = pose.speed
        name = pose.name
        self.ui.log_encoder.append(f"{str(robot_pose)} \n {str(speed)}")
    
    def monitor_encoders(self):
        print("monitor data started")
        self.encoder_sub = self.node.create_subscription(
            RobotPose,
            '/encoder_data',
            self.encoder_gui,
            1)

    def log_encoder(self, pose:RobotPose):
        # self.init_timer.destroy()
        robot_pose = pose.mode#  # [pose.position.x, pose.position.y, pose.position.z, pose.orientation.x, pose.orientation.y]
        # robot_pose = f"{str(robot_pose)}\n"
        print(robot_pose)
        self.ui.log_console.clear()
        # self.ui.table_encoder.append(f'{str(robot_pose)}')
        self.ui.log_console.append(f"{str(robot_pose)}")  
    # live camera extraction 
    def update_pixmap_cam_top(self, image_message: Image):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(image_message, desired_encoding="passthrough")
        except:
            print("subscription faild")
        # self.node.get_logger().info("Recieved")

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
        rclpy.spin(self.node)
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
    # app = QtWidgets.QApplication(sys.argv)
    # #app = QApplication(sys.argv)
    # win = MainWindow()
    
    # splash_screen = SplashScreen()
    # splash_screen.show()
    # app.processEvents()
    # # Display splash screen while UI loads
    # splash_screen.finish(win.ui)
    # win.show()
    # # app.exec()
    
    
    # sys.exit(app.exec_())
    main()