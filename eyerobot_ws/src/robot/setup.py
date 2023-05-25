from setuptools import setup

package_name = 'robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alireza',
    maintainer_email='alireza.alikhani@tum.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_encoder = robot.robot_encoder:main',
            'robot_driver  = robot.robot_driver:main',
            'robot_move_z_tran = robot.robot_move_z_tran: main',
            'robot_slam_trn = robot.robot_slam_trn : main'
        ],
    },
)
