#!/usr/bin/env python3

import rospy
from game_control.srv import GetUserScore, GetUserScoreResponse, SetGameDifficulty, SetGameDifficultyResponse
from game_control.msg import user_msg
from std_msgs.msg import String, Int64
import pygame
import random

class GameNode:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        pygame.font.init()

        # Game constants
        self.WIDTH = 800
        self.HEIGHT = 600
        self.BRICK_WIDTH = 80
        self.BRICK_HEIGHT = 30
        self.BALL_SIZE = 15
        self.PLAYER_WIDTH = 100
        self.PLAYER_HEIGHT = 20
        self.PLAYER_SPEED = 5

        # Game state variables
        self.game_state = "welcome"  # States: welcome, playing, game_over
        self.score = 0
        self.lives = 3
        self.level = 1
        self.player = None
        self.ball = None
        self.ball_speed_x = None
        self.ball_speed_y = None
        self.bricks = []  # Initialize bricks as an empty list
        self.user_name = ""
        self.user_username = ""
        self.user_age = ""
        self.score_sent = False  # Flag to track if score has been sent

        # Initialize game objects
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Breakout")
        self.player = pygame.Rect(self.WIDTH // 2 - self.PLAYER_WIDTH // 2, self.HEIGHT - 40, self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
        self.ball = pygame.Rect(self.WIDTH // 2 - self.BALL_SIZE // 2, self.HEIGHT // 2 - self.BALL_SIZE // 2, self.BALL_SIZE, self.BALL_SIZE)
        self.reset_ball()
        self.initialize_bricks()  # Initialize bricks at the start

        # Game loop
        self.clock = pygame.time.Clock()

        # ROS Publishers and Subscribers
        self.result_pub = rospy.Publisher('result_information', Int64, queue_size=10)
        rospy.Subscriber('user_information', user_msg, self.user_info_callback)
        rospy.Subscriber('keyboard_control', String, self.keyboard_callback)

        # Service handlers
        self.srv_get_user_score = rospy.Service('user_score', GetUserScore, self.handle_get_user_score)
        self.srv_set_game_difficulty = rospy.Service('difficulty', SetGameDifficulty, self.handle_set_game_difficulty)

    def handle_get_user_score(self, req):
        rospy.loginfo(f"Returning score for user: {req.user_name}")
        return GetUserScoreResponse(self.score)

    def handle_set_game_difficulty(self, req):
        if self.game_state == "welcome":
            rospy.loginfo(f"Setting game difficulty to {req.change_difficulty}")
            if req.change_difficulty == "easy":
                self.level = 1
                rospy.set_param('change_player_color', 1)
            elif req.change_difficulty == "medium":
                self.level = 2
                rospy.set_param('change_player_color', 2)
            elif req.change_difficulty == "hard":
                self.level = 3
                rospy.set_param('change_player_color', 3)
            return SetGameDifficultyResponse(True)
        else:
            rospy.logwarn("Cannot change difficulty. Not in 'welcome' phase.")
            return SetGameDifficultyResponse(False)

    def user_info_callback(self, msg):
        self.user_name = msg.name
        self.user_username = msg.username
        self.user_age = msg.age
        rospy.set_param('user_name', self.user_name)
        rospy.set_param('screen_param', 'phase1')
        rospy.set_param('change_player_color', 1)
        rospy.loginfo(f"User Info: Name - {self.user_name}, Username - {self.user_username}, Age - {self.user_age}")

    def keyboard_callback(self, msg):
        if (msg.data == "START" or msg.data == "SPACE") and self.game_state == "welcome":
            self.game_state = "playing"
            rospy.set_param('screen_param', 'playing')
            self.reset_ball()
            rospy.loginfo("Game started!")
        elif msg.data == "LEFT" and self.game_state == "playing":
            self.move_left()
        elif msg.data == "RIGHT" and self.game_state == "playing":
            self.move_right()
        elif msg.data == "RESTART" and self.game_state == "game_over":
            rospy.loginfo("Restarting game...")
            self.reset_game()

    def reset_game(self):
        self.game_state = "welcome"
        self.score = 0
        self.lives = 3
        self.level = 1
        self.bricks = []
        self.reset_ball()
        self.initialize_bricks()
        self.score_sent = False
        rospy.set_param('screen_param', 'phase1')
        rospy.loginfo("Game reset to initial state.")

    def initialize_bricks(self):
        self.bricks = []
        for row in range(5):
            for col in range(self.WIDTH // self.BRICK_WIDTH):
                brick = pygame.Rect(col * self.BRICK_WIDTH, row * self.BRICK_HEIGHT + 50, self.BRICK_WIDTH - 2, self.BRICK_HEIGHT - 2)
                self.bricks.append(brick)
        rospy.loginfo("Bricks initialized.")

    def move_left(self):
        if self.player.left > 0:
            self.player.x -= self.PLAYER_SPEED

    def move_right(self):
        if self.player.right < self.WIDTH:
            self.player.x += self.PLAYER_SPEED

    def reset_ball(self):
        self.ball.center = (self.WIDTH // 2, self.HEIGHT // 2)
        self.ball_speed_x = random.choice([-3, 3])
        self.ball_speed_y = -3

    def draw_text(self, text, color, x, y):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def welcome_phase(self):
        self.screen.fill((0, 0, 0))
        self.draw_text(f"Welcome {self.user_name}!", (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2 - 50)
        self.draw_text("Press 'START' or 'SPACE' to begin the game", (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2 + 50)

    def game_phase(self):
        self.screen.fill((0, 0, 0))
        self.draw_text(f"Score: {self.score}", (255, 255, 255), 70, 20)
        self.draw_text(f"Lives: {self.lives}", (255, 255, 255), self.WIDTH - 70, 20)
        self.draw_text(f"Level: {self.level}", (255, 255, 255), self.WIDTH // 2, 20)
        pygame.draw.rect(self.screen, (255, 0, 0), self.player)
        pygame.draw.ellipse(self.screen, (255, 255, 255), self.ball)
        for brick in self.bricks:
            pygame.draw.rect(self.screen, (255, 0, 0), brick)

    def final_phase(self):
        self.screen.fill((0, 0, 0))
        self.draw_text(f"Game Over! Final Score: {self.score}", (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2)
        self.result_pub.publish(self.score)
        self.score_sent = True

    def game_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.game_state == "welcome":
                self.welcome_phase()
            elif self.game_state == "playing":
                self.game_phase()
            elif self.game_state == "game_over" and not self.score_sent:
                self.final_phase()

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    rospy.init_node('game_node')
    game_node = GameNode()
    game_node.game_loop()
