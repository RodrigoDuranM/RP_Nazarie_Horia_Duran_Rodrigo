#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import pygame

class ControlNodePygame:
    def __init__(self):
        rospy.init_node('control_node_pygame')
        self.pub = rospy.Publisher('keyboard_control', String, queue_size=10)
        self.run()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Control Node (Pygame)")

        rospy.loginfo("Control node using pygame ready. Use arrow keys to move or 's' to start the game.")

        running = True
        while not rospy.is_shutdown() and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Continuously check if the arrow keys are being held down. This allows for better movement of the board.
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.pub.publish("LEFT")
            elif keys[pygame.K_RIGHT]:
                self.pub.publish("RIGHT")
            elif keys[pygame.K_s]:
                self.pub.publish("START")
            elif keys[pygame.K_r]:
                self.pub.publish("RESTART")

        pygame.quit()

if __name__ == "__main__":
    try:
        ControlNodePygame()
    except rospy.ROSInterruptException:
        pass
