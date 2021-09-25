#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg): 
    print (len(msg.ranges))
    distance_to_wall = msg.ranges[360]
    print (msg.ranges[360], "m")
    twister = Twist()
    if distance_to_wall > 1:
        twister.linear.x = 1
    else:
        twister.linear.x = 0
        twister.angular.z = 1
    pub.publish(twister)
  


rospy.init_node('topics_quiz_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
rospy.spin()