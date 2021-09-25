#! /usr/bin/env python
import rospy
import actionlib
from std_msgs.msg import Empty
from actions_quiz.msg import CustomActionMsgResult, CustomActionMsgFeedback, CustomActionMsgAction

class Ardrone_Action_Server(object):
  _feedback = CustomActionMsgFeedback()
  def __init__(self):
    # creates the action server
    self._as = actionlib.SimpleActionServer("/action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
    self._as.start()
    
  def goal_callback(self, goal):
    print("goal = ", goal)
    action_string = goal.goal
    
    if action_string == "TAKEOFF":
        pub = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
        pub.publish(Empty())
    if action_string == "LAND":
        pub = rospy.Publisher('/drone/land', Empty, queue_size=1)
        pub.publish(Empty())
    
    r = rospy.Rate(1)
    success = True
    self._feedback.feedback = action_string
    self._as.set_succeeded(True)
      
if __name__ == '__main__':
  rospy.init_node('actions_quiz')
  Ardrone_Action_Server()
  rospy.spin()