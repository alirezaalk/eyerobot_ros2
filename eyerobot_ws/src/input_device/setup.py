from setuptools import setup

package_name = 'input_device'

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
            'input_device_node = input_device.input_device_node:main',
            'input_robot_interface = input_device.input_robot_interface:main'
        ],
    },
)
