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
```
. ~/catkin_ws/devel/setup.bash
```
```
 roslaunch cyglidar_d1 cyglidar.launch
```
*    That will launch an empty window in rviz that looks like this: 
* In the third one run a rosbag with lidar data, or plug in the physical cyglidar d1 sensor: 
```
 rosbag play insert_rosbag_name_here.bag 
```

* In the fourth one navigate to occupancy_test.py and run it: 
```
cd  ~/catkin/src/path/to/file/
python occupancy_test.py
```
You're output should look something like this: 
And in the same directory you put occupancy_test in you should see a scatter plot called scatter.py. That will have your map of 2D lidar data generated once you quite the occupancy_test.py program in the terminal, which you do using ctrl c. 
The scatter plot should look like a 2D representation of your lidar data: 

## How it works
