## ROS2-Humble-Node

This is a simple ROS 2 node that demonstrates the basic structure of a ROS 2 Python node. It publishes a message periodically.

## Prerequisites

Make sure you have ROS 2 installed. If not, you can follow the installation instructions on the [ROS 2 website](https://index.ros.org/doc/ros2/Installation/).

## Building

To build the ROS 2 package containing this node, follow these steps:

1. Create a ROS 2 workspace:

   ```
   bash
   mkdir -p ~/ros2_workspace/src
   cd ~/ros2_workspace/src
   ```
2. Clone this repository into your workspace:

   ```
   git clone https://github.com/raguladhithyam/ROS2-Humble-Node.git
   ```

3. Build the ROS 2 Package

   ```
   cd ~/ros2_workspace
   colcon build
   ```

## Running the Node

After building the package, you can run the node as follows:

1. Source your ROS 2 workspace:

   ```
   source ~/ros2_workspace/install/setup.bash
   ```

2. Run the node:

   ```
   ros2 run my_robot_controller test_node
   ```
   The node will start publishing messages periodically.


