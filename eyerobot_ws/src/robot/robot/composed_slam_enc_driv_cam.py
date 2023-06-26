
import threading
import rclpy
from robot.robot_encoder import RobotEncoder
from robot.robot_driver import RobotDriver
from basler.cam_top_pub import CamTopPub
from robot.robot_slam_service import RobotSLAM
from rclpy.executors import MultiThreadedExecutor
def main(args = None):
    rclpy.init(args=args)
    node0 = CamTopPub()
    node1 = RobotSLAM()
    node2 = RobotDriver()
    node3 = RobotEncoder()
    # node0 = rclpy.create_node('ui')
    #node1 = rclpy.create_node('robot_driver')
    # node1 = rclpy.create_node('camera_top')
    executor = MultiThreadedExecutor()
    executor.add_node(node0)
    executor.add_node(node1)
    executor.add_node(node2)
    executor.add_node(node3)
    # Spin in a separate thread
    # executor_thread = threading.Thread(target=executor.spin, daemon=True)
    # executor_thread.start()
    # rate = node0.create_rate(2)
    try:
        
        executor.spin()
        #print('Help me body, you are my only hope')
        #rate.sleep()
    except KeyboardInterrupt:
        executor.shutdown()
        node0.destroy_node()
        node1.destroy_node()
        node2.destroy_node()
        rclpy.shutdown()
    # node1.destroy_node()

