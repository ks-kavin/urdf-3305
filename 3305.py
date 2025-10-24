from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    
    urdf_file = '/home/kavin-ks/ros2_ws/src/my_robot_description/urdf/simple_robot.urdf'
    
    # Read the URDF content
    with open(urdf_file, 'r') as infp:
        robot_description = infp.read()

    return LaunchDescription([
        # Publish robot state
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),

        # Launch RViz2 for visualization
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        )
    ])
