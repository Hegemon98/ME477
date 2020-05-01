# ME477

This repo serves the purpose of the ME477 ROS final. It was created through tutorials contained in the the text [ricopic.one/robotics](http://ricopic.one/robotics). It is organized and structured to fulfill several requirenments as detailed [here](http://ricopic.one/courses/robotics_mini_course/#final-project)

## Requirements

The text assumes the use of ROS Melodic Morenia and Ubuntu 18.04.4 LTS (Bionic Beaver). Instructions for installing this development environment are included in the text.

## Installation

To make the packages available within a ROS distribution, complete the following steps.

1. Create a ROS workspace with a `src` directory.
2. Download and unzip or clone this repository to the `src` directory.
```bash
git clone https://github.com/ricopicone/robotics-book-code.git
```
3. In the workspace, make.
```bash
catkin_make
```
4. Source your workspace.
```bash
source devel/setup.bash
```
Following these steps should result in the packages being available within the target ROS distribution.
