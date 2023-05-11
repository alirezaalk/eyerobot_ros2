#!/usr/bin/python3
'''
'!/usr/bin/python3' we keep original python3, to kill all not found gcc folder. 
because gcc folder in ubuntu is set to /usr/lib/.. and we don't need to change it. 
## TODO find a way to kill this error when using #!/usr/bin/env python: Error: version `GLIBCXX_3.4.29' not found (required by /home/alireza/anaconda3/envs/robot-planner/bin/../lib/libmysqlclient.so.21)
'''

import sys
from rclpy.node import Node
from PyQt5 import QtWidgets
import rclpy
from ui_handler import UIHandler
from packages.parse_images import parse_images
from packages.splash_screen import SplashScreen

class UILoader(Node):
    def __init__(self):
        # Initilize the node
        super().__init__("ui_node")
        self.get_logger().info("Medical Autonomy and Precision Surgery Laboratory - Robot Control UI")
        print("Medical Autonomy and Precision Surgery Laboratory - Robot Control UI")
        self.counter_ = 0
        self.create_timer(1, self.timer_callback)
        self.create_timer(0.05, self.show_ui)
        # bring up the ui
        self.app = QtWidgets.QApplication(sys.argv)

        # Build splash screen and UI
        splash_screen = SplashScreen()
        self.ui = UIHandler()
        splash_screen.show()
        self.app.processEvents()

        # Display splash screen while UI loads
        splash_screen.finish(self.ui.ui)

        # Display UI
        # ui.show()

        # Enter main loop
        # self.app.exec()


    def timer_callback(self):
        self.get_logger().info(f'times running {self.counter_} minutes!')
        self.counter_ += 1
        
    def show_ui(self):
        self.ui.show()
        self.app.exec()
        
# Starts command and control UI
# Also displays our splash screen

def main(args=None):
    rclpy.init(args=args)
    node = UILoader()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
