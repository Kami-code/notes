#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
import time
import numpy as np

def my_callback(request):
    print("My_callback has been called", request)
    print("duration = ", request.side)
    duration = request.side
    repetitions = request.repetitions
    twister_forward = Twist()
    twister_forward.linear.x = 1
    twister_rotate = Twist()
    twister_rotate.angular.z = np.pi / 2
    rotate_time_const = 1.6
    for i in range(repetitions):
        pub.publish(twister_forward)
        time.sleep(duration)
        pub.publish(twister_rotate)
        time.sleep(rotate_time_const)
        pub.publish(twister_forward)
        time.sleep(duration)
        pub.publish(twister_rotate)
        time.sleep(rotate_time_const)
        pub.publish(twister_forward)
        time.sleep(duration)
        pub.publish(twister_rotate)
        time.sleep(rotate_time_const)
        pub.publish(twister_forward)
        time.sleep(duration)
        pub.publish(twister_rotate)
        time.sleep(rotate_time_const)
    pub.publish(Twist())
    return BB8CustomServiceMessageResponse() # the service Response class, in this case EmptyResponse

rospy.init_node('service_server') 
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.