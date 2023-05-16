

import rclpy
import numpy as np
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from rclpy.node import Node
from basler.basler_camera.basler_camera import BaslerCamera 
class CamTopPub(Node):
    def __init__(self):
        super().__init__("cam_top_pub")
        self.get_logger().info("Camera Top View Node has started!")
        self.cam_top_topic_ = "/cam_top"
        self.frame_per_second_ = 20
        self.cam_top_pub_ = self.create_publisher(Image, self.cam_top_topic_, 10)
        self.image_ = None
        self.bridge_ = CvBridge()

        self.timer_ = self.create_timer(1/self.frame_per_second_, self.send_frame)
        self.cam_ = BaslerCamera()
    
    def send_frame(self):
        self.image = self.cam_.get_latest_frame()
        if self.image is not None:
            self.cam_top_pub_.publish(self.bridge_.cv2_to_imgmsg(self.image))
            self.get_logger().info('frame Sent')

def main(args = None):
    try:
        BaslerCamera().stop_camera()
        rclpy.init(args=args)
        node = CamTopPub()
        rclpy.spin(node)
    except KeyboardInterrupt:
        BaslerCamera().stop_camera()
        rclpy.shutdown()
    

if __name__ == "__main__":
    main()