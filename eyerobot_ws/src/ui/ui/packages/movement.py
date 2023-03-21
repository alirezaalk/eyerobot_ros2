from PyQt5 import uic
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QMouseEvent
from std_msgs.msg import Int16



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