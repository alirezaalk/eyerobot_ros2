import rclpy

from robot.robot_slam_trn import RobotSLAMTrn
from robot.robot_slam_rcm import RobotSLAMRcm
from robot.robot_encoder import RobotEncoder
from robot.robot_driver import RobotDriver
from rclpy.executors import SingleThreadedExecutor


def main(args=None):
    rclpy.init(args=args)
    try:
        re = RobotEncoder()
        rd = RobotDriver()
        executor = SingleThreadedExecutor()
        executor.add_node(re)
        executor.add_node(rd)

        try:
            executor.spin()
        finally:
            executor.shutdown()
            re.destroy_node()
            rd.destroy_node()

    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()