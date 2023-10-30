#!/usr/bin/env python3
#!/usr/bin/env python

#Interpreter line to say to use python3
import rclpy #It is the python library for ros2
#install ros ( microsoft ) extension
# to create nodes, we need to implement oops
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("first_node")
        self.counter_ = 0
        # self.get_logger().info("Ros2") # self gets functionalities of node class
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyNode() #node is created and is called from node class
    rclpy.spin(node) #this will run node untill we kill it via keyboard
    rclpy.shutdown() # destroys node

if __name__ == '__main__': # will be helpful to run file directly from terminal
    main()
 