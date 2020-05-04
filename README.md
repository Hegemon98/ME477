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
Using the above launch command, the four nodes within this package will launch and begin printing to the terminal. Expected output should resemble the following:
```bash
1
Real: 0.021548465
Imaginary: 0.984262465
```
For individual usage of these nodes the following command format may be used with roscore running in another terminal.
```bash
rosrun <package name> <node name>
```
Example:
```bash
rosrun my_topics topic_publisher.py
```
### Usage
It should be noted that the subscriber files will not be functional without also having their associated publisher file also running.

# ROS package: my_services
The my_services package contains two nodes:
1.service_client.py: this node accepts strings of characters from the user via the command line, counts the number of words, and outputs the result.
2.service_server.py: this node contains a service called word_count which is used by service_client.py to count the number of input words. 

These nodes are usefull in demonstrating basic service node functionality and communication and can be used as starting points for more advanced use cases.
### Getting started with my_services
```bash
roslaunch my_services services.launch input:='<insert text here>'
```
Using the above launch command, the two nodes within this package will launch and begin printing to the terminal. Expected output should resemble the following:
```bash
user input has 2 words
```
For individual usage of these nodes the following command format may be used with roscore running in another terminal.
```bash
rosrun <package name> <node name> <user input>
```
Example:
```bash
rosrun my_services service_client.py hello world
```
### Usage
It should be noted that the user input argument should only be used when calling the client.

# ROS package: my_actions
The my_actions package contains two nodes:
1. fancy_action_client.py:
2. fancy_action_server.py:
|Short introductory paragraph about your package. What does it do? Why is it useful?|
### Getting started with my_actions
```bash
roslaunch my_actions fancy_action.launch
```
Using the above launch command, the two nodes within this package will launch and begin printing to the terminal. Expected output should resemble the following:
```bash
[Feedback] Time elapsed: 0.000023
[Feedback] Time remaining: 4.999977
```
### Usage

|Usage information for key methods and commands.|
