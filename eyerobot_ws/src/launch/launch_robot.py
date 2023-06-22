from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot',
            executable='robot_encoder',
            namespace="",
            name='robot_encoder',
            # prefix = ["sudo"],
            # Launch the node with root access (GPIO) in a shell
            #prefix=["sudo -E env \"PYTHONPATH=$PYTHONPATH\" \"LD_LIBRARY_PATH=$LD_LIBRARY_PATH\" \"PATH=$PATH\" \"USER=$USER\"  bash -c "],
            shell=True,
        ),
        Node(
            package='robot',
            executable='robot_driver',
            namespace="",
            name='robot_driver',
            # prefix = ["sudo"],
            # Launch the node with root access (GPIO) in a shell
            #prefix=["sudo -E env \"PYTHONPATH=$PYTHONPATH\" \"LD_LIBRARY_PATH=$LD_LIBRARY_PATH\" \"PATH=$PATH\" \"USER=$USER\"  bash -c "],
            shell=True,
        ),
        # Node(
        #     package='robot',
        #     executable='robot_trn_service',
        #     namespace="",
        #     name='robot_slam_service',
        #     # prefix = ["sudo"],
        #     # Launch the node with root access (GPIO) in a shell
        #     #prefix=["sudo -E env \"PYTHONPATH=$PYTHONPATH\" \"LD_LIBRARY_PATH=$LD_LIBRARY_PATH\" \"PATH=$PATH\" \"USER=$USER\"  bash -c "],
        #     shell=True,
        # ),
        # Node(
        #     package='ui',
        #     executable='gui_node',
        #     namespace="",
        #     name='gui_node',
        #     # prefix = ["sudo"],
        #     # Launch the node with root access (GPIO) in a shell
        #     #prefix=["sudo -E env \"PYTHONPATH=$PYTHONPATH\" \"LD_LIBRARY_PATH=$LD_LIBRARY_PATH\" \"PATH=$PATH\" \"USER=$USER\"  bash -c "],
        #     shell=True,
        # ),
        
    ])

if __name__ == "__main__":
    js = generate_launch_description()
    print(js)