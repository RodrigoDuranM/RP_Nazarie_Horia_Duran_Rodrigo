#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('control_node')
    pub = rospy.Publisher('keyboard_control', String, queue_size=10)

    rospy.loginfo("Control node ready. Type LEFT, RIGHT, or START to control the game.")
    while not rospy.is_shutdown():
        command = input("Enter command: ").strip().upper()
        if command in ["LEFT", "RIGHT", "START"]:
            pub.publish(command)
        else:
            rospy.logwarn("Invalid command. Use LEFT, RIGHT, or START.")

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass