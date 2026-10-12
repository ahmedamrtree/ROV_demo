import rclpy
from rclpy.node import Node
from custom_msgs.msg import Motion

class motion_node(Node):
    def __init__(self):
        super().__init__("motion_node")
        self.create_subscription(Motion, "joystick_motion", self.joystick_listen, 10)

    def joystick_listen (self, msg:Motion):
        self.get_logger().info(f"{msg}")


def main():
    rclpy.init()
    node = motion_node()
    rclpy.spin(node)
    
if __name__ == "__main__":
    main()
