import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose  
from std_msgs.msg import Float32  
import math

class DistanceCalculator(Node):
    def __init__(self):
        super().__init__('distance_calculator')
        
        #subscription
        self.pose_subscriber = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10)
        
        #publisher
        self.distance_publisher = self.create_publisher(
            Float32,
            '/turtle1/distance_from_origin',
            10)
        
        self.get_logger().info("DistanceCalculator node has been started.")

    def pose_callback(self, msg):
        x = msg.x
        y = msg.y
        distance = math.sqrt(x**2 + y**2)
        self.get_logger().info(f"Computed Distance from Origin: {distance:.2f}")

        distance_msg = Float32()
        distance_msg.data = distance
        self.distance_publisher.publish(distance_msg)

def main(args=None):
    rclpy.init(args=args)
    node = DistanceCalculator()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down DistanceCalculator node.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

