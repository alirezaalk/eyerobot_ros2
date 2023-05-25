# !/usr/bin/env python

import numpy as np
import rclpy
from rclpy.node import Node
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
from PyQt5 import uic
from .configs.ui_config import UiConfig
# Updates a qt-label with images received from a ROS channel
class D445CameraSubscriber(Node):
    def __init__(self):
        super().__init__("d445CameraSubscriber")
        self.get_logger().info("Realsense Camera Subscriber Node has been started!")
        self.bridge = CvBridge()
        self.ui = uic.loadUi(UiConfig().UI_DIR + 'main_ui.ui')
        # self.target_label = target_label
        # self.channel_name = channel_name
        self.cam_subscriber_ = self.create_subscription(Image, "/d445_images", self.update_pixmap, 1)
        self.subscriber = None
        # self.ui.start_camera_button.clicked.connect(self.start_camera)


    def update_pixmap(self, image_message: Image):
        #print("HI")
        # self.cam_subscriber_ = self.create_subscription(Image, "/d445_images", self.update_pixmap, 1)
        cv_image = self.bridge.imgmsg_to_cv2(image_message, desired_encoding="passthrough")
        #print(cv_image)
        # cv2.imshow('frame', cv_image)
        # cv2.waitKey(1)
        # self.target_label = QLabel()
        
        # # scaling the image while showing in the ui
        scale_factor = 0.20
        self.show_frame(self.ui.camera_image, cv_image)
        #target_label.setPixmap(convert_cv_qt(cv_image))
        # target_label.setMaximumHeight(cv_image.shape[0] * scale_factor)
        # target_label.setMaximumWidth(cv_image.shape[1] * scale_factor)
        self.get_logger().info("Recieved!")
        # return cv_image

    def show_frame(self,target_label: QLabel , image ):
        
        # # scaling the image while showing in the ui
        scale_factor = 0.20
        target_label.setPixmap(convert_cv_qt(image))
        # target_label.setMaximumHeight(cv_image.shape[0] * scale_factor)
        # target_label.setMaximumWidth(cv_image.shape[1] * scale_factor)

    def start(self):
        self.cam_subscriber= self.create_subscription(Image, "/d445_images", self.update_pixmap, 1)


    def stop(self):
        if self.subscriber:
            self.subscriber.unregister()


# Source: https://gist.github.com/docPhil99/ca4da12c9d6f29b9cea137b617c7b8b1
def convert_cv_qt(cv_image: np.ndarray):
    """Convert from an opencv image to QPixmap"""
    h, w, ch = cv_image.shape
    bytes_per_line = ch * w
    qt_image = QtGui.QImage(cv_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    return QPixmap.fromImage(qt_image)

def main(args=None):
    topic_name = 'd445_images'
    rclpy.init(args=args)
    node = D445CameraSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()