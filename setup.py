from setuptools import find_packages, setup

package_name = 'CS460HW4'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/launch.py']))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/maze.wbt', 
    'worlds/tut.wbt',
    'worlds/maze2.wbt'
]))
data_files.append(('share/' + package_name, ['package.xml']))

data_files.append(('share/' + package_name + '/resource', [
    'resource/turtlebot_webots.urdf',
    'resource/ros2control.yml',
]))

data_files.append(('share/' + package_name + '/rviz', [
    'rviz/turtlebot3_apriltags.rviz', 
]))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='Monica Anderson-UA',
    maintainer_email='anderson@ua.edu',
    description='Webots Apriltags',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],
        'console_scripts': ['CS460HW4 = CS460HW4.CS460HW4:main']
    },

)
