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
        self.score_sent = False  # Track if score is sent to RESULT_NODE

        # Initialize game objects
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Breakout")
        self.player = pygame.Rect(self.WIDTH // 2 - self.PLAYER_WIDTH // 2, self.HEIGHT - 40, self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
        self.ball = pygame.Rect(self.WIDTH // 2 - self.BALL_SIZE // 2, self.HEIGHT // 2 - self.BALL_SIZE // 2, self.BALL_SIZE, self.BALL_SIZE)
        self.bricks = self.generate_bricks()
        self.reset_ball()

        # ROS Publishers and Subscribers
        self.result_pub = rospy.Publisher('result_information', Int64, queue_size=10)
        rospy.Subscriber('user_information', user_msg, self.user_info_callback)
        rospy.Subscriber('keyboard_control', String, self.keyboard_callback)

        # Service handlers
        rospy.Service('user_score', GetUserScore, self.handle_get_user_score)
        rospy.Service('difficulty', SetGameDifficulty, self.handle_set_game_difficulty)

        # Load ROS parameters
        self.load_parameters()

        # Game loop clock
        self.clock = pygame.time.Clock()

    def load_parameters(self):
        self.user_name = rospy.get_param('user_name', 'Player')
        self.change_player_color = rospy.get_param('change_player_color', 1)
        self.screen_param = rospy.get_param('screen_param', 'phase1')

    def handle_get_user_score(self, req):
        rospy.loginfo(f"Returning score for user: {req.user_name}")
        return GetUserScoreResponse(self.score)

    def handle_set_game_difficulty(self, req):
        if self.game_state == "welcome":
            difficulty_map = {"easy": 1, "medium": 2, "hard": 3}
            if req.change_difficulty in difficulty_map:
                self.level = difficulty_map[req.change_difficulty]
                rospy.set_param('change_player_color', self.level)
                rospy.loginfo(f"Difficulty set to {req.change_difficulty}")
                return SetGameDifficultyResponse(True)
        rospy.logwarn("Cannot change difficulty. Not in 'welcome' phase.")
        return SetGameDifficultyResponse(False)

    def user_info_callback(self, msg):
        self.user_name = msg.name
        rospy.set_param('user_name', self.user_name)

    def keyboard_callback(self, msg):
        if msg.data == "START" and self.game_state == "welcome":
            self.game_state = "playing"
            self.reset_game()
        elif msg.data in ["LEFT", "RIGHT"] and self.game_state == "playing":
            self.move_player(msg.data)

    def move_player(self, direction):
        if direction == "LEFT" and self.player.left > 0:
            self.player.x -= self.PLAYER_SPEED
        elif direction == "RIGHT" and self.player.right < self.WIDTH:
            self.player.x += self.PLAYER_SPEED

    def reset_ball(self):
        self.ball.center = (self.WIDTH // 2, self.HEIGHT // 2)
        self.ball_speed_x = random.choice([-3, 3])
        self.ball_speed_y = -3

    def reset_game(self):
        self.score = 0
        self.lives = 3
        self.level = 1
        self.bricks = self.generate_bricks()
        self.reset_ball()
        rospy.set_param('screen_param', 'phase1')

    def generate_bricks(self):
        bricks = []
        for row in range(5):
            for col in range(self.WIDTH // self.BRICK_WIDTH):
                brick = pygame.Rect(col * self.BRICK_WIDTH, row * self.BRICK_HEIGHT + 50, self.BRICK_WIDTH - 2, self.BRICK_HEIGHT - 2)
                bricks.append(brick)
        return bricks

    def game_phase(self):
        self.load_parameters()
        player_color_map = {1: (255, 0, 0), 2: (128, 0, 128), 3: (0, 0, 255)}
        player_color = player_color_map.get(self.change_player_color, (255, 255, 255))

        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, player_color, self.player)
        pygame.draw.ellipse(self.screen, (255, 255, 255), self.ball)
        # Update ball movement and handle collisions...
        if len(self.bricks) == 0 or self.lives <= 0:
            self.game_state = "game_over"

    def final_phase(self):
        self.screen.fill((0, 0, 0))
        self.draw_text(f"Game Over! Score: {self.score}", (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2)
        self.result_pub.publish(self.score)
        self.score_sent = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.game_state = "welcome"
            self.reset_game()
        elif keys[pygame.K_ESCAPE]:
            rospy.signal_shutdown("User exited the game.")

    def draw_text(self, text, color, x, y):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def game_loop(self):
        while not rospy.is_shutdown():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rospy.signal_shutdown("Game exited by user.")
            if self.game_state == "welcome":
                self.welcome_phase()
            elif self.game_state == "playing":
                self.game_phase()
            elif self.game_state == "game_over":
                self.final_phase()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    rospy.init_node('game_node')
    game = GameNode()
    game.game_loop()
