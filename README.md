# Repository Purpose
The purpose of this repository is to fullfill the requirements of the ME 477 ROS mini-course final as listed [here](http://ricopic.one/courses/robotics_mini_course/#final-project)

## Requirements
These packages have been designed for use on systems with the following:
1. ROS Melodic Morenia
2. Ubuntu 18.04.4 LTS (Bionic Beaver).

## Installation

In order to make these packages accessible within the ROS installation, the following steps must be completed:

1. Create a ROS workspace with a `src` directory.
2. Clone this repository to the `src` directory.
```bash
git clone https://github.com/Hegemon98/ME477.git
```
3. In the workspace, make.
```bash
catkin_make
```
4. Source the workspace.
```bash
source devel/setup.bash
```
# ROS package: my_topics
The my_topics package contains four nodes:
1. message_publisher.py: this node publishes a message with an imaginary and a real value
2. message_subscriber.py: this node subscribes to message_publisher.py and displays the recieved values in the terminal
3. topic_publisher.py: this node publishes a topic called counter which increments upward after every publish
4. topic_subscriber.py: this node subscribes to topic_publisher.py and dispays the recieved values in the terminal

These nodes are usefull in demonstrating basic topic and message node functionality and communication and can be used as starting points for more advanced use cases.
### Getting started with my_topics
```bash
roslaunch my_topics topics.launch
```

|A short guide to using your package. Include important commands, etc.|

### Usage

|Usage information for key methods and commands.|

# ROS package: my_services
The my_services package contains two nodes:
1. service_client.py: this node
2. service_server.py: this node
These nodes are usefull in demonstrating basic service node functionality and communication and can be used as starting points for more advanced use cases.
### Getting started with my_services
```bash
roslaunch my_topics topics.launch
```
|A short guide to using your package. Include important commands, etc.|

### Usage

|Usage information for key methods and commands.|

# ROS package: my_actions

|Short introductory paragraph about your package. What does it do? Why is it useful?|
## Getting started with my_actions
```bash
roslaunch my_actions topics.launch
```

|A short guide to using your package. Include important commands, etc.|

## Usage

|Usage information for key methods and commands.|
