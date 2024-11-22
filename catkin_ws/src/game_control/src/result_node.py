#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

def callback(data):
    rospy.loginfo(f"Final Score: {data.data}")

def main():
    rospy.init_node('result_game')
    rospy.Subscriber('result_information', Int64, callback)

    rospy.loginfo("Result node ready to receive final scores.")
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass