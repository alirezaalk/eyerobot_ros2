#! usr/bin/env python3
import robot.core.robot.lcm_ros_wrapper as lrw
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose


class RobotEncoder(Node):
    """
    A Class which recieves data from lcm and publish it through the ros2 into the topic
    parameters
    -------
    frequency : int
        defines how many times per seconds subscribing from the topic
    """
    def __init__(self):
        super().__init__("robot_encoder")
        self.get_logger().info("Encoder data is publishing")
        self.topic_name = '/encoder_data'
        self.frequency = 100
        self.encoder_pub = self.create_publisher(Pose, self.topic_name, 10)
        self.timer = self.create_timer((1/self.frequency), self.encoders_data)


    ## TODO create a 5DOF msg type in ROS2
    ## TODO for error handling we need to be sure that the lcm is connected
    def encoders_data(self):
        """
        decoding data/ due to lacking appropriate msg type in original ros2, Pose is used but needs to be changed
        """
        pose = Pose()
        data,*other = lrw.encoder_data()
        #print(data)
        try:
            # z 
            pose.position.x = data[0]
            # y
            pose.position.y = data[1]
            pose.position.z = data[2]
            # x
            pose.orientation.x = data[3]
            pose.orientation.y = data[4]
            self.get_logger().info(
                f"Z:{pose.position.x} - Y: {pose.position.y}/{pose.position.z} - X:{pose.orientation.x}/{pose.orientation.y}"
                )
            # publish a data to the topic
            self.encoder_pub.publish(pose)   
        except : 
            self.get_logger().error("Check all connection!") 



def main(args=None):
    rclpy.init(args=args)
    node = RobotEncoder()
    rclpy.spin(node)
    rclpy.shutdown()
