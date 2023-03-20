# !/usr/bin/env python

import numpy as np
import rclpy
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


# Updates a qt-label with images received from a ROS channel
class CameraSubscriber:
    def __init__(self, target_label: QLabel, channel_name: str):
        self.bridge = CvBridge()
        self.target_label = target_label
        self.channel_name = channel_name

        self.subscriber = None

    def update_pixmap(self, image_message: Image):
        cv_image = self.bridge.imgmsg_to_cv2(image_message, desired_encoding="passthrough")
        # scaling the image while showing in the ui
        scale_factor = 0.20
        self.target_label.setPixmap(convert_cv_qt(cv_image))
        self.target_label.setMaximumHeight(cv_image.shape[0] * scale_factor)
        self.target_label.setMaximumWidth(cv_image.shape[1] * scale_factor)

    def start(self):
        self.subscriber = rospy.Subscriber(self.channel_name, Image, self.update_pixmap)

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
