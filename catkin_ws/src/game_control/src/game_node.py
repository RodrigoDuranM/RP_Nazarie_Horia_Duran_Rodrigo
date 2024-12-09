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
        self.score_sent = False  # Flag to track if score has been sent
        self.bricks = []  # Initialize bricks as an empty list

        # Dictionary to store scores by user name
        self.scores = {}

        # Initialize game objects
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Breakout")
        self.player = pygame.Rect(self.WIDTH // 2 - self.PLAYER_WIDTH // 2, self.HEIGHT - 40, self.PLAYER_WIDTH, self.PLAYER_HEIGHT)
        self.ball = pygame.Rect(self.WIDTH // 2 - self.BALL_SIZE // 2, self.HEIGHT // 2 - self.BALL_SIZE // 2, self.BALL_SIZE, self.BALL_SIZE)
        self.reset_ball()

        # Game loop
        self.clock = pygame.time.Clock()

        # Topics
        self.result_pub = rospy.Publisher('result_information', Int64, queue_size=10)
        rospy.Subscriber('user_information', user_msg, self.user_info_callback)
        rospy.Subscriber('keyboard_control', String, self.keyboard_callback)

        # Services
        self.srv_get_user_score = rospy.Service('/game_node/user_score', GetUserScore, self.handle_get_user_score)
        self.srv_set_game_difficulty = rospy.Service('/game_node/difficulty', SetGameDifficulty, self.handle_set_game_difficulty)

        # Parameters
        self.screen_param = rospy.get_param('game_node/screen_param', 'phase1')  
        self.change_player_color = rospy.get_param('game_node/change_player_color', 1)  
        self.user_name = rospy.get_param('game_node/user_name', 'Player')  

        rospy.loginfo(f"Game initialized with user_name: {self.user_name}, screen_param: {self.screen_param}, change_player_color: {self.change_player_color}")

    def handle_get_user_score(self, req):
        """Handles the service to get the user's score."""
        user_name = req.user_name
        # Retrieve the score for the user from the scores dictionary
        score = self.scores.get(user_name, 0)  # Default score if the player doesn't exist
        rospy.loginfo(f"Fetching score for {user_name}: {score}")
        return GetUserScoreResponse(score)

    def handle_set_game_difficulty(self, req):
        if self.game_state == "welcome":
            rospy.loginfo(f"Setting game difficulty to {req.change_difficulty}")
            if req.change_difficulty == "easy":
                self.level = 1
                rospy.set_param('game_node/change_player_color', 1)  # Set color to red for easy
            elif req.change_difficulty == "medium":
                self.level = 2
                rospy.set_param('game_node/change_player_color', 2)  # Set color to purple for medium
            elif req.change_difficulty == "hard":
                self.level = 3
                rospy.set_param('game_node/change_player_color', 3)  # Set color to blue for hard
            return SetGameDifficultyResponse(True)
        else:
            rospy.logwarn("Cannot change difficulty. Not in 'welcome' phase.")
            return SetGameDifficultyResponse(False)

    def update_score(self, user_name, score):
        """Update the score for a specific user."""
        self.scores[user_name] = score
        rospy.loginfo(f"Updated score for {user_name}: {score}")

    def user_info_callback(self, msg):
        """Callback to handle user information and set parameters."""
        rospy.set_param('game_node/user_name', msg.name)  # Set the parameter when the name is received
        self.user_name = rospy.get_param('game_node/user_name')  # Re-fetch updated parameter
        rospy.loginfo(f"User Info: Name - {self.user_name}, Username - {msg.username}, Age - {msg.age}")

        # Initialize the user's score if it doesn't exist
        if self.user_name not in self.scores:
            self.scores[self.user_name] = self.score  # Set initial score for the player
        self.update_score(self.user_name, self.score)  # Update score for the player

    def keyboard_callback(self, msg):
        """Callback to handle keyboard inputs for movement and game control."""
        if msg.data == "START" and self.game_state == "welcome":
            self.game_state = "playing"
            rospy.set_param('game_node/screen_param', 'phase2')  # Update phase to playing
            self.reset_ball()
            rospy.loginfo("Game started!")
        elif msg.data == "LEFT" and self.game_state == "playing":
            self.move_left()
        elif msg.data == "RIGHT" and self.game_state == "playing":
            self.move_right()

        # Handle restart or exit commands when the game is over
        if self.game_state == "game_over":
            if msg.data == "RESTART":
                self.restart_game()
            elif msg.data == "EXIT":
                rospy.signal_shutdown("User exited the game.")

    def move_left(self):
        """Move the player paddle left."""
        if self.player.left > 0:
            self.player.x -= self.PLAYER_SPEED

    def move_right(self):
        """Move the player paddle right."""
        if self.player.right < self.WIDTH:
            self.player.x += self.PLAYER_SPEED

    def reset_ball(self):
        """Reset the ball to the center."""
        self.ball.center = (self.WIDTH // 2, self.HEIGHT // 2)
        self.ball_speed_x = random.choice([-3, 3])
        self.ball_speed_y = -3

    def generate_bricks(self):
        """Generate bricks for the game."""
        bricks = []
        for row in range(5):
            for col in range(self.WIDTH // self.BRICK_WIDTH):
                brick = pygame.Rect(col * self.BRICK_WIDTH, row * self.BRICK_HEIGHT + 50, self.BRICK_WIDTH - 2, self.BRICK_HEIGHT - 2)
                bricks.append(brick)
        return bricks

    def game_phase(self):
        """Game logic for the playing phase."""
        # Re-fetch the parameter to ensure we are using the updated value
        self.user_name = rospy.get_param('game_node/user_name', 'Player')
        
        # Fetch the player color dynamically on every update (so it updates when the parameter changes)
        player_color_value = rospy.get_param('game_node/change_player_color', 1)  # Default to red (1)

        # Map the integer value to actual colors
        if player_color_value == 1:
            player_color_rgb = (255, 0, 0)  # Red
        elif player_color_value == 2:
            player_color_rgb = (128, 0, 128)  # Purple
        elif player_color_value == 3:
            player_color_rgb = (0, 0, 255)  # Blue
        else:
            player_color_rgb = (255, 255, 255)  # Default to white if invalid value

        # Set the player color to the updated value
        self.screen.fill((0, 0, 0))

        pygame.draw.rect(self.screen, player_color_rgb, self.player)  # Draw player paddle with selected color
        pygame.draw.ellipse(self.screen, (255, 255, 255), self.ball)

        for brick in self.bricks:
            pygame.draw.rect(self.screen, (255, 0, 0), brick)

        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y

        if self.ball.left <= 0 or self.ball.right >= self.WIDTH:
            self.ball_speed_x = -self.ball_speed_x
        if self.ball.top <= 0:
            self.ball_speed_y = -self.ball_speed_y

        if self.ball.colliderect(self.player):
            self.ball_speed_y = -self.ball_speed_y

        for brick in self.bricks[:]:
            if self.ball.colliderect(brick):
                self.bricks.remove(brick)
                self.ball_speed_y = -self.ball_speed_y
                self.score += 10
                self.update_score(self.user_name, self.score)  # Ensure score is updated in the dictionary

        if self.ball.bottom >= self.HEIGHT:
            self.lives -= 1
            if self.lives > 0:
                self.reset_ball()
            else:
                self.game_state = "game_over"

        if len(self.bricks) == 0:
            self.level += 1
            self.bricks = self.generate_bricks()
            self.reset_ball()

        self.draw_text(f"Level: {self.level}", (255, 255, 255), 70, 20)
        self.draw_text(f"Lives: {self.lives}", (255, 255, 255), self.WIDTH - 70, 20)
        self.draw_text(f"Score: {self.score}", (255, 255, 255), self.WIDTH // 2, 20)

    def final_phase(self):
        """Final phase of the game, after the game is over."""
        rospy.set_param('game_node/screen_param', 'phase3')  # Update phase to game over
        self.screen.fill((0, 0, 0))
        self.draw_text(f"Game Over! Score: {self.score}", (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2)

        if not self.score_sent:
            self.result_pub.publish(self.score)
            self.score_sent = True

        self.draw_text("Press 'RESTART' to restart or 'EXIT' to exit.", (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2 + 50)

    def restart_game(self):
        """Restart the game."""
        self.game_state = "welcome"
        self.score = 0
        self.lives = 3
        self.level = 1
        self.bricks = self.generate_bricks()
        self.reset_ball()
        rospy.set_param('game_node/screen_param', 'phase1')  # Reset screen phase
        rospy.loginfo("Game restarted.")

    def draw_text(self, text, color, x, y):
        """Draw text on the screen."""
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def welcome_phase(self):
        """Welcome phase logic."""
        # Ensure the user_name parameter is updated in the welcome phase
        self.user_name = rospy.get_param('game_node/user_name', 'Player')  # Fetch updated parameter
        self.screen.fill((0, 0, 0))
        self.draw_text(f"Welcome {self.user_name}!", (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2 - 50)
        self.draw_text("Press 'START' to begin the game", (255, 255, 255), self.WIDTH // 2, self.HEIGHT // 2 + 50)

    def game_loop(self):
        """Main game loop."""
        while not rospy.is_shutdown():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rospy.signal_shutdown("Game exited.")
            if self.game_state == "welcome":
                self.welcome_phase()
            elif self.game_state == "playing":
                self.game_phase()
            elif self.game_state == "game_over":
                self.final_phase()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    rospy.init_node('game_node')
    game_node = GameNode()
    game_node.game_loop()
