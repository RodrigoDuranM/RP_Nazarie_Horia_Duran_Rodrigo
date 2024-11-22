#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import pygame

def main():
    rospy.init_node('control_node_pygame')
    pub = rospy.Publisher('keyboard_control', String, queue_size=10)

    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Control Node (Pygame)")

    rospy.loginfo("Control node using pygame ready. Use arrow keys or S to control the game.")

    running = True
    while not rospy.is_shutdown() and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Continuously check if the arrow keys are being held down
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pub.publish("LEFT")
        elif keys[pygame.K_RIGHT]:
            pub.publish("RIGHT")
        elif keys[pygame.K_s]:
            pub.publish("START")

    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass