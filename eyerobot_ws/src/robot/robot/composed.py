import rclpy

from robot.robot_slam_trn import RobotSLAMTrn
from robot.robot_slam_rcm import RobotSLAMRcm

from rclpy.executors import SingleThreadedExecutor


def main(args=None):
    rclpy.init(args=args)
    try:
        trn = RobotSLAMTrn(120000, 'z')
        # rcm = RobotSLAMRcm()

        executor = SingleThreadedExecutor()
        executor.add_node(trn)
        # executor.add_node(minimal_subscriber)

        try:
            executor.spin()
        finally:
            executor.shutdown()
            trn.destroy_node()
            # rcm.destroy_node()

    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()