#!/usr/bin/env python3

import rospy
from game_control.srv import GetUserScore, SetGameDifficulty
from game_control.msg import user_msg
from std_msgs.msg import Int64

class ResultNode:
    def __init__(self):
        rospy.init_node('result_game')
        rospy.Subscriber('result_information', Int64, self.callback)
        rospy.Subscriber('user_information', user_msg, self.user_info_callback)
        rospy.loginfo("Result node ready to receive final scores and user information.")
        
        # Wait for services to be available
        rospy.wait_for_service('user_score')
        rospy.wait_for_service('difficulty')

        # Create service proxies
        self.get_user_score = rospy.ServiceProxy('user_score', GetUserScore)
        self.set_game_difficulty = rospy.ServiceProxy('difficulty', SetGameDifficulty)

    def callback(self, data):
        rospy.loginfo(f"Final Score: {data.data}")

    def user_info_callback(self, data):
        rospy.loginfo(f"User Information - Name: {data.name}, Username: {data.username}, Age: {data.age}")
        
        # Request the user score from the game_node
        try:
            score_response = self.get_user_score(data.name)  # Correctly send 'user_name'
            rospy.loginfo(f"User {data.name}'s score: {score_response.score}")
        except rospy.ServiceException as e:
            rospy.logwarn(f"Service call failed: {e}")
        
        # Request to set game difficulty
        try:
            difficulty_response = self.set_game_difficulty("medium")  # You can change this dynamically
            if difficulty_response.success:
                rospy.loginfo(f"Game difficulty set to medium successfully.")
            else:
                rospy.logwarn("Failed to change game difficulty.")
        except rospy.ServiceException as e:
            rospy.logwarn(f"Service call failed: {e}")

    def run(self):
        rospy.spin()

if __name__ == "__main__":
    try:
        result_node = ResultNode()
        result_node.run()
    except rospy.ROSInterruptException:
        pass
