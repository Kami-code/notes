#! /usr/bin/env python
import rospkg
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest, MyCustomServiceMessageResponse # you import the service message python classes generated from Empty.srv.
import sys
import rospy

rospy.init_node('service_client_call')
rospy.wait_for_service('/my_service')
my_service = rospy.ServiceProxy('/my_service', MyCustomServiceMessage)
my_service_request = MyCustomServiceMessageRequest()
my_service_request.duration = 6
result = my_service(my_service_request)
print(result)