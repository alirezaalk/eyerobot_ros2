import os

import rclpy
from rclpy.node import Node

from PyQt5 import uic
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtGui import QIcon, QPixmap
from std_msgs.msg import Int16
from sensor_msgs.msg import Image
from camera_subscriber import CameraSubscriber
from packages.canvas import Canvas



# The main UI represents the centerpiece of user interaction
# Interprocess communication is done through the ROS publisher/subscriber interface
class MainUI(Node):
    def __init__(self):
        # super().__init__("pose_subscriber")
        # self.get_logger().info("main ui has been started")
        # UI is generated directly from ui file
        self.ui = uic.loadUi("/home/alireza/projects/eyerobot_planner/eyerobot_workspace/src/eyerobot_ui/src/robot_control.ui")

        # Initialize node
        # self.create_publisher(Int16, "/UI", 10)
        # rospy.init_node('UI', anonymous=False)

        # Initialize canvas
        # self.canvas = Canvas(self.ui)

        # Print to console of UI
        # self.ui.log_console.append("Medical Autonomy and Precision Surgery Laboratory - Robot Control UI\n")

        # Create a subscriber capable of receiving camera images
        # self.create_subscription(Image, "/d445_images", self.get_camera_frames_callback)
        # self.camera_listener = CameraSubscriber(self.ui.camera_image, "/d445_images")

        # Create a publisher capable of transmitting control sequences
        # self.control_publisher = rospy.Publisher("/ui_control", Int16, queue_size=64)

        # Connect UI signals
        # self.ui.start_camera_button.clicked.connect(self.start_camera)
        # self.ui.stop_camera.clicked.connect(self.stop_camera)
        # self.ui.control_up.mousePressEvent = self.emit_signal_up
        # self.ui.control_down.mousePressEvent = self.emit_signal_down
        # self.ui.control_left.mousePressEvent = self.emit_signal_left
        # self.ui.control_right.mousePressEvent = self.emit_signal_right

        # # sending ui message object
        # self.msg = Int16()
        # # Intercept close event
        # self.ui.closeEvent = self.close_event


    # TODO add camera callback 
    def get_camera_frames_callback(self):
        self.get_logger().info("waiting for frames")


    # Register camera subscriber
    def start_camera(self):
        self.ui.start_camera_button.hide()
        self.ui.stop_camera.show()
        self.camera_listener.start()
        log_string = "Camera is running"
        self.ui.log_console.append(log_string)
    
    def stop_camera(self):
        self.camera_listener.stop()
        self.ui.camera_layout = QPixmap('icons/camera_icon.png')
        print('camera stopped')

        self.ui.start_camera_button.show()
        self.ui.stop_camera.hide()
        log_string = "Camera Stopped"
        self.ui.log_console.append(log_string)


    def emit_signal_up(self, mouse_event: QMouseEvent):
        self.msg = 0
        self.control_publisher.publish(self.msg)
        log_string = "Transmitting control sequence: up"
        print(log_string)
        self.ui.log_console.append(log_string)

    def emit_signal_down(self, mouse_event: QMouseEvent):
        self.msg = 1
        self.control_publisher.publish(self.msg)
        log_string = "Transmitting control sequence: down"
        print(log_string)
        self.ui.log_console.append(log_string)

    def emit_signal_left(self, mouse_event: QMouseEvent):
        self.msg = 2
        self.control_publisher.publish(self.msg)
        log_string = "Transmitting control sequence: left"
        print(log_string)
        self.ui.log_console.append(log_string)

    def emit_signal_right(self, mouse_event: QMouseEvent):
        self.msg = 3
        self.control_publisher.publish(self.msg)
        log_string = "Transmitting control sequence: right"
        print(log_string)
        self.ui.log_console.append(log_string)

    # Display contained UI
    def show(self):
        self.ui.show()

    # UI is closed by user
    def close_event(self, event: QEvent):
        self.camera_listener.stop()
        event.accept()


def main(args=None):
    rclpy.init(args=args)
    node = MainUI()
    rclpy.shutdown()
