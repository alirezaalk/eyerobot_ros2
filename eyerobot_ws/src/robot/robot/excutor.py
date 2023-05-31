import robot.robot_slam_rcm as rcm
import robot.robot_slam_trn as tran


rcm.main([-1,0], 'xz')
tran.main(12000, 'z')