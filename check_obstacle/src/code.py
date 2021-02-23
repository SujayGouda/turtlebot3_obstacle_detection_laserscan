#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
	move.linear.x = 0.2
	if msg.ranges[359] < 1:
		print("Obstacle detected, stopped moving")
		move.linear.x = 0
	else:
		print("Moving forward.. Scanning range:{}".format(msg.ranges[359]))
	pub.publish(move)

rospy.init_node('check_obstacle')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()
