#!/usr/bin/env python3

import rospy
from game_control.msg import user_msg
from std_msgs.msg import Int64
from game_control.srv import GetUserScore

class ResultNode:
    def __init__(self):
        rospy.init_node('result_game')
        
        # Subscribers
        rospy.Subscriber('result_information', Int64, self.callback)
        rospy.Subscriber('user_information', user_msg, self.user_info_callback)
        
        # Initialize user information
        self.username = ""

        rospy.loginfo("Result node ready to receive final scores and user information.")
        rospy.spin()

    def callback(self, data):
        rospy.loginfo(f"Final Score: {data.data}")

    def user_info_callback(self, data):
        self.username = data.username
        rospy.loginfo(f"User Information - Name: {data.name}, Username: {data.username}, Age: {data.age}")
        # After receiving user information, fetch the score from the service
        self.get_score_client(self.username)

    def get_score_client(self, username):
        rospy.wait_for_service('user_score')
        try:
            get_score = rospy.ServiceProxy('user_score', GetUserScore)
            response = get_score(username)
            rospy.loginfo(f"Score for {username}: {response.score}%")
        except rospy.ServiceException as e:
            rospy.logerr(f"Service call failed: {e}")

if __name__ == "__main__":
    try:
        ResultNode()
    except rospy.ROSInterruptException:
        pass
