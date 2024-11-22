#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class ControlNode:
    def __init__(self):
        rospy.init_node('control_node')
        self.pub = rospy.Publisher('keyboard_control', String, queue_size=10)
        self.run()

    def run(self):
        rospy.loginfo("Control node ready. Type LEFT, RIGHT, or START to control the game.")
        while not rospy.is_shutdown():
            command = input("Enter command: ").strip().upper()
            if command in ["LEFT", "RIGHT", "START"]:
                self.pub.publish(command)
            else:
                rospy.logwarn("Invalid command. Use LEFT, RIGHT, or START.")

if __name__ == "__main__":
    try:
        ControlNode()
    except rospy.ROSInterruptException:
        pass
