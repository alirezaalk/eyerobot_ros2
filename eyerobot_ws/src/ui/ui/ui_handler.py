import os
import sys
import rclpy
from rclpy.node import Node
from PyQt5 import uic
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtGui import QIcon, QPixmap
from std_msgs.msg import Int16
from sensor_msgs.msg import Image
from .camera_subscriber import D445CameraSubscriber
## add this library to enable running composed nodes in other scripts
from rclpy.executors import SingleThreadedExecutor
from .packages.canvas import Canvas
from .configs.vision_config import VisionConfig
from .configs.ui_config import UiConfig
from PyQt5 import QtWidgets
# from main_ui import MainUI
from .packages.parse_images import parse_images
from .packages.splash_screen import SplashScreen


from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from cv_bridge import CvBridge
import numpy as np
# The main UI represents the centerpiece of user interaction
# Interprocess communication is done through the ROS publisher/subscriber interface


class UIHandler():
    def __init__(self):
        # UI is generated directly from ui file
        self.ui = uic.loadUi(UiConfig().UI_DIR + 'main_ui.ui')
        self.counter_ = 0
        
        # Initialize canvas from config
        if UiConfig().CANVAS:
            self.canvas = Canvas(self.ui)
        # initilize oce vol renderer
        if UiConfig().PARSE_OCT_VOL:
            parse_images()

        # self.target_label = QLabel
        # self.channel_name = channel_name
        # Create a subscriber capable of receiving camera images
        #self.camera_listener = D445CameraSubscriber(self.ui.camera_image, "main_camera")
        #self.camera
        
        # Connect UI signals
        ## Camera Button
        self.ui.start_camera_button.clicked.connect(self.start_camera)
        self.ui.stop_camera.clicked.connect(self.stop_camera)
        ## Arrow buttons
        self.ui.control_up.mousePressEvent = self.emit_signal_up
        self.ui.control_down.mousePressEvent = self.emit_signal_down
        self.ui.control_left.mousePressEvent = self.emit_signal_left
        self.ui.control_right.mousePressEvent = self.emit_signal_right

        # sending ui message object
        # self.msg = Int16()
        # # Intercept close event
        # self.ui.closeEvent = self.close_event

    def ui_show(self):
        # self.app = QtWidgets.QApplication(sys.argv)
        # splash_screen = SplashScreen()
        # self.app.processEvents()
        # splash_screen.finish(self.ui.ui)
        self.ui.show()
        self.app.exec()


    def timer_callback(self):
        self.get_logger().info(f"Running time is {self.counter_} mins")


    # TODO add camera callback 
    def get_camera_frames_callback(self):
        self.get_logger().info("waiting for frames")




    # Register camera subscriber
    def start_camera(self):
        #rclpy.init(args=None)
        try:
            print("hi")
            self.cv_image = D445CameraSubscriber()
            self.executor = SingleThreadedExecutor()
            self.executor.add_node(self.cv_image)
            try:
                self.executor.spin()
            finally:
                self.executor.shutdown()
                self.cv_image.destroy_node()
        finally: 
            rclpy.shutdown()

        # self.target_label = self.ui.camera_image
        # # # scaling the image while showing in the ui
        # scale_factor = 0.20
        # self.target_label.setPixmap(convert_cv_qt(self.cv_image))
        # self.target_label.setMaximumHeight(self.cv_image.shape[0] * scale_factor)
        # self.target_label.setMaximumWidth(self.cv_image.shape[1] * scale_factor)
        # UINodeLoader().start_camera()
        # self.ui.start_camera_button.hide()
        # self.ui.stop_camera.show()
        # self.camera_listener.start()
        log_string = "Camera is running"
        self.ui.log_console.append(log_string)
    
    def stop_camera(self):
        self.executor.shutdown()
        # self.camera_listener.stop()
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
        # self.camera_listener.stop()
        event.accept()


# Source: https://gist.github.com/docPhil99/ca4da12c9d6f29b9cea137b617c7b8b1
def convert_cv_qt(cv_image: np.ndarray):
    """Convert from an opencv image to QPixmap"""
    h, w, ch = cv_image.shape
    bytes_per_line = ch * w
    qt_image = QtGui.QImage(cv_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    return QPixmap.fromImage(qt_image)


def main(args=None):
    pass
    # rclpy.init(args=args)
    # node = UIHandler()
    # rclpy.spin(node)
    # rclpy.shutdown()
    # return node
    # # MainUI()


if __name__ == "__main__":
    main()
