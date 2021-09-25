#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

def my_callback(request):
    print("My_callback has been called")
    twister = Twist()
    twister.linear.x = 1
    twister.angular.z = 1
    print("Twist", twister)
    pub.publish(twister)
    return EmptyResponse() # the service Response class, in this case EmptyResponse

rospy.init_node('service_server') 
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.