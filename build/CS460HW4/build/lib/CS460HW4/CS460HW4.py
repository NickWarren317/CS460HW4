import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image, CameraInfo
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from std_msgs.msg import String
from apriltag_msgs.msg import AprilTagDetectionArray
from cv_bridge import CvBridge
import cv2
import time
import math
from rclpy.qos import QoSProfile

LINEAR_VEL = 0.22
STOP_DISTANCE = 0.2
LIDAR_ERROR = 0.05
LIDAR_AVOID_DISTANCE = 0.6

LIDAR_RIGHT_TURN_DISTANCE = 0.55
LIDAR_LEFT_TURN_DISTANCE = 0.55
LOCATION_PING = 5

SAFE_STOP_DISTANCE = STOP_DISTANCE + LIDAR_ERROR
RIGHT_SIDE_INDEX = 270
RIGHT_FRONT_INDEX = 210
LEFT_FRONT_INDEX=150
LEFT_SIDE_INDEX=90


class RandomWalk(Node):

    def __init__(self):
        super().__init__('random_walk_node')
        
        self.april_tag_subscriber = self.create_subscription(
            AprilTagDetectionArray,
            '/detections',  # Replace with your actual topic
            self.april_tag_callback,
            10
        )

        # Lidar and Odometry setup
        self.scan_cleaned = []
        self.stall = False
        self.path = []
        self.last_recorded_time = time.time()
        self.find_wall = True
        self.bot_turning = False
        self.turned = False
        self.out_file = f"coords.txt"
        self.turtlebot_moving = False
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # Subscriptions for LIDAR and Odometry
        self.subscriber1 = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback1,
            QoSProfile(depth=10)
        )
        self.subscriber2 = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback2,
            QoSProfile(depth=10)
        )

        # Timer for periodic tasks
        timer_period = 0.5
        self.pose_saved = ''
        self.cmd = Twist()
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.last_wall_dist = 0


    def listener_callback1(self, msg1):
        scan = msg1.ranges
        self.scan_cleaned = [3.5 if reading == float('Inf') else (0.0 if math.isnan(reading) else reading) for reading in scan]

    def listener_callback2(self, msg2):
        position = msg2.pose.pose.position
        self.pose_saved = position     

    def camera_callback(self, msg):
        # Convert ROS image to OpenCV format
        
        # You can now process the image using OpenCV (e.g., for visualization or debugging)
        #self.get_logger().info("Received camera image!")
        cv2.waitKey(1)

    def april_tag_callback(self, msg):
        # Check if any AprilTags were detected
        self.get_logger().info(f"Detected {len(msg.detections)} AprilTags.")
        if msg.detections:
            for detection in msg.detections:
                tag_id = detection.id
                self.get_logger().info(f"Detected AprilTag with ID: {tag_id}")
                
                # Example: Stop the robot if a tag with a specific ID is detected
                if tag_id == 1:  # Replace with your target tag ID
                    self.stop_robot()

    def stop_robot(self):
        # Stop the robot when a specific tag is detected
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.publisher_.publish(self.cmd)
        self.get_logger().info("Robot stopped due to AprilTag detection!")

    def timer_callback(self):
        if len(self.scan_cleaned) == 0:
            self.turtlebot_moving = False
            return

        left_lidar_min = min(self.scan_cleaned[LEFT_SIDE_INDEX:LEFT_FRONT_INDEX])
        right_lidar_min = min(self.scan_cleaned[RIGHT_FRONT_INDEX:RIGHT_SIDE_INDEX])
        front_lidar_min = min(self.scan_cleaned[LEFT_FRONT_INDEX:RIGHT_FRONT_INDEX])

        if self.find_wall:
            self.go_straight()
            if front_lidar_min < LIDAR_AVOID_DISTANCE:
                self.last_wall_dist = right_lidar_min
                self.find_wall = False
        else:
            if front_lidar_min < LIDAR_AVOID_DISTANCE:
                self.bot_turning = False
                if right_lidar_min < LIDAR_RIGHT_TURN_DISTANCE and left_lidar_min < LIDAR_LEFT_TURN_DISTANCE:
                    self.bot_turning = True
                    self.cmd.linear.x = 0.25
                    self.cmd.angular.z = 5.0
                elif right_lidar_min < LIDAR_RIGHT_TURN_DISTANCE:
                    self.bot_turning = True
                    self.cmd.linear.x = 0.5
                    self.cmd.angular.z = 5.0
                elif left_lidar_min < LIDAR_LEFT_TURN_DISTANCE:
                    self.bot_turning = True
                    self.cmd.linear.x = 0.5
                    self.cmd.angular.z = -5.0
                else:
                    self.bot_turning = True
                    self.cmd.linear.x = 0.5
                    self.cmd.angular.z = 5.0
            else:
                if right_lidar_min < LIDAR_RIGHT_TURN_DISTANCE and left_lidar_min < LIDAR_LEFT_TURN_DISTANCE:
                    self.go_straight()
                elif right_lidar_min < LIDAR_RIGHT_TURN_DISTANCE:
                    self.go_straight()
                elif left_lidar_min < LIDAR_LEFT_TURN_DISTANCE:
                    self.bot_turning = True
                    self.cmd.linear.x = 0.5
                    self.cmd.angular.z = -5.0
                else:
                    self.bot_turning = True
                    self.cmd.linear.x = 0.5
                    self.cmd.angular.z = -5.0

        self.publisher_.publish(self.cmd)

        self.get_logger().info(f"Distance of the obstacle: {front_lidar_min}")
        #self.get_logger().info(f"I receive: {str(self.odom_data)}")
        if self.stall:
            self.get_logger().info("Stall reported")

    def go_straight(self):
        self.bot_turning = False
        self.cmd.linear.x = 0.5
        reading = min(self.scan_cleaned[RIGHT_FRONT_INDEX:RIGHT_SIDE_INDEX])
        self.cmd.angular.z = 0.0
        self.publisher_.publish(self.cmd)
        self.turtlebot_moving = True


def main(args=None):
    rclpy.init(args=args)
    random_walk_node = RandomWalk()

    try:
        rclpy.spin(random_walk_node)
    except KeyboardInterrupt:
        random_walk_node.get_logger().info("Shutting down...")
    finally:
        random_walk_node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
