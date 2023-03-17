#!/usr/bin/env python
# EASY-INSTALL-ENTRY-SCRIPT: 'venv==0.0.0','console_scripts','venv'
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import sys
sys.path.append('/home/alireza/projects/eyerobot-ros2/eyerobot_ws/src/frame/frame')
from realsense.realsense import RealSense_Camera
## TODO 1- fix how to address other packages in other folders/ 2- in order to fix pyrealsense2 module, I commented the conda in .bashrc and install it on the ubuntu which should be fixed and compatible with the conda enviroments.

class FrameExtractor(Node):
    def __init__(self):
        super().__init__("d445_publisher")
        self.get_logger().info("d445 frame publisher has been started!")
        self.frame_pub_ = self.create_publisher(Image, "/d445_publisher", 10)
        self.image_ = None
        self.bridge_ = CvBridge()
        self.timer_ = self.create_timer(0.1, self.send_frame)
        self.camera_ = RealSense_Camera()

    def send_frame(self):
        # msg = Image()
        self.image, color_depth, depth = self.camera_.get_latest_frame(show_image =True)
        if self.image is not None:
            self.frame_pub_.publish(self.bridge_.cv2_to_imgmsg(self.image))
        

def main(args=None):
    rclpy.init(args=args)
    node = FrameExtractor()
    rclpy.spin(node)
    rclpy.shutdown()
    RealSense_Camera().stop_stream()


if __name__ == "__main__":
    main()