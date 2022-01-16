# RoboFish-Occupancy-Grid
Occupancy Grid for Undersea Robotic Fish
## Installation Requirements 
Dual boot or use a VM to install Ubuntu 20.04 on your machine. 
Install ROS Melodic. 
## Usage 
You're going to need to open four terminal windows: 
* In the first one run roscore: 
```
roscore
```

* In the second one run the cyglidar d1 ros driver launch command: 
* You might need to run the setup bash command first: 
  . ~/catkin_ws/devel/setup.bash
```
 roslaunch cyglidar_d1 cyglidar.launch
```

* In the third one run a rosbag with lidar data, or plug in the physical cyglidar d1 sensor: 
* In the fourth one navigate to occupancy_test.py and run it: 
