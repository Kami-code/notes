#! /usr/bin/env python
import rospkg
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest,BB8CustomServiceMessageResponse
import sys
import rospy

rospy.init_node('service_client_call')
rospy.wait_for_service('/move_bb8_in_square_custom')
my_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
my_service_request = BB8CustomServiceMessageRequest()
my_service_request.side = 1
my_service_request.repetitions = 5
result = my_service(my_service_request)
print(result)