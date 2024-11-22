#!/usr/bin/env python3

import rospy
from game_control.msg import user_msg

class InfoUser:
    def __init__(self):
        self.pub = rospy.Publisher('user_information', user_msg, queue_size=10)
        self.user = user_msg()

    def collect_user_info(self):
        self.user.name = input("Enter your name: ")
        self.user.username = input("Enter your username: ")
        self.user.age = int(input("Enter your age: "))

    def publish_user_info(self):
        rospy.loginfo(f"Publishing user information: {self.user}")
        rate = rospy.Rate(1)  # 1 Hz
        self.pub.publish(self.user)
        while not rospy.is_shutdown():
            rate.sleep()

def main():
    rospy.init_node('info_user')
    info_user = InfoUser()
    info_user.collect_user_info()
    info_user.publish_user_info()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
