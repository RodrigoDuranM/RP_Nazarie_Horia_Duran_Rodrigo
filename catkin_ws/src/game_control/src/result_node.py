#!/usr/bin/env python3

import rospy
from game_control.msg import user_msg
from std_msgs.msg import Int64

class ResultNode:
    def __init__(self):
        rospy.init_node('result_game')
        rospy.Subscriber('result_information', Int64, self.callback)
        rospy.Subscriber('user_information', user_msg, self.user_info_callback)
        rospy.loginfo("Result node ready to receive final scores and user information.")
        rospy.spin()

    def callback(self, data):
        rospy.loginfo(f"Final Score: {data.data}")

    def user_info_callback(self, data):
        rospy.loginfo(f"User Information - Name: {data.name}, Username: {data.username}, Age: {data.age}")

if __name__ == "__main__":
    try:
        ResultNode()
    except rospy.ROSInterruptException:
        pass
