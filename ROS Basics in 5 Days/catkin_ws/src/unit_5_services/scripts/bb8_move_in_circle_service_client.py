#! /usr/bin/env python
import rospkg
from std_srvs.srv import Empty, EmptyRequest, EmptyResponse # you import the service message python classes generated from Empty.srv.
import sys
import rospy


# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /trajectory_by_name to be running
rospy.wait_for_service('/move_bb8_in_circle')
# Create the connection to the service
traj_by_name_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
# Create an object of type TrajByNameRequest
traj_by_name_object = EmptyRequest()
# Fill the variable traj_name of this object with the desired value
# Send through the connection the name of the trajectory to be executed by the robot
result = traj_by_name_service(traj_by_name_object)
# Print the result given by the service called
print(result)