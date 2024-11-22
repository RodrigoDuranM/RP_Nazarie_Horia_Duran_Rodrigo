#!/usr/bin/env python3

import rospy
from game_control.msg import user_msg

def main():
    rospy.init_node('info_user')
    pub = rospy.Publisher('user_information', user_msg, queue_size=10)
    
    user = user_msg()
    user.name = input("Enter your name: ")
    user.username = input("Enter your username: ")
    user.age = int(input("Enter your age: "))

    rospy.loginfo(f"Publishing user information: {user}")
    rate = rospy.Rate(1)
    pub.publish(user)
    while not rospy.is_shutdown():
        rate.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
