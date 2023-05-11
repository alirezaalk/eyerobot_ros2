import rclpy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QMouseEvent, QPainter, QPen, QPolygon
from std_msgs.msg import UInt64MultiArray, MultiArrayDimension


class Canvas:
    def __init__(self, ui):
        self.ui = ui

        # Create a publisher capable of transmitting control sequences
        # self.canvas_publisher = rospy.Publisher("/ui_canvas", UInt64MultiArray, queue_size=64)

        # Connect UI signals
        self.ui.canvas_image.mousePressEvent = self.click_on_canvas
        self.ui.canvas_image.mouseMoveEvent = self.move_on_canvas

        self.ui.save_canvas.mousePressEvent = self.save_canvas
        self.ui.reset_canvas.mousePressEvent = self.reset_canvas

        # Exchange paint function
        self.canvas_paintEvent_function = self.ui.canvas_image.paintEvent
        self.ui.canvas_image.paintEvent = self.update_drawing

        # Store user input: x,y relative to image on canvas
        self.user_points = []

    def update_drawing(self, event):
        self.canvas_paintEvent_function(event)
        painter = QPainter(self.ui.canvas_image)
        painter.setPen(QPen(Qt.red, 1, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(0, 255, 0, 128)))
        polygon = QPolygon(self.user_points)
        painter.drawPolygon(polygon)

    def click_on_canvas(self, mouse_event: QMouseEvent):
        # self.user_input.append((mouse_event.pos().x(), mouse_event.pos().y()))
        self.user_points.append(mouse_event.pos())
        self.ui.canvas_image.update()

    def move_on_canvas(self, mouse_event: QMouseEvent):
        # self.user_input.append((mouse_event.pos().x(), mouse_event.pos().y()))
        self.user_points.append(mouse_event.pos())
        self.ui.canvas_image.update()

    def save_canvas(self, mouse_event: QMouseEvent):
        points = [[point.x(), point.y()] for point in self.user_points]
        points_flattened = [coordinate for point in points for coordinate in point]

        message_array = UInt64MultiArray()
        message_array.layout.dim.append(MultiArrayDimension("Points", len(points_flattened), len(points_flattened) * 2))
        message_array.layout.dim.append(MultiArrayDimension("X/Y Coordinate", 2, 2))
        message_array.data = points_flattened

        self.canvas_publisher.publish(message_array)

    def reset_canvas(self, mouse_event: QMouseEvent):
        self.user_points.clear()
        self.ui.canvas_image.update()
