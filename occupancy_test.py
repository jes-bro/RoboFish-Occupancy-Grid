#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import math
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, radians, pi

def callback(data):
	cloud_points = list(pc2.read_points(data, skip_nans=True, field_names = ("x", "y", "z")))
	plot_coordinates(cloud_points)


def plot_coordinates(points):
	x, y, z = zip(*points)
	create_occupancy_grid(x,y,z)
	#centroid = find_centroids(x,y,z)
	print(x,y,z)
	pass

def create_occupancy_grid(x,y,z):
	fig = plt.figure()
	axes = fig.add_subplot(1,1,1)
	axes.scatter(x,y)
	plt.savefig('scatter.png')
	plt.close(fig)
	exit()

def find_centroids(x,y,z):
	x_center = sum(x) / len(x)
	y_center = sum(y) / len(y)
	z_center = sum(z) / len(z)
	centroid = (x_center, y_center, z_center)

rospy.init_node('listener', anonymous=True)
rospy.Subscriber("/scan_2D", PointCloud2, callback)
rospy.spin()