import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player
player_width = 100
player_height = 20
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - 40, player_width, player_height)
player_speed = 5

# Ball
ball_size = 15
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
ball_speed_x = 3
ball_speed_y = -3

# Bricks
brick_width = 80
brick_height = 30
bricks = []
for row in range(5):
    for col in range(WIDTH // brick_width):
        brick = pygame.Rect(col * brick_width, row * brick_height + 50, brick_width - 2, brick_height - 2)
        bricks.append(brick)

# Game variables
score = 0
lives = 3
level = 1
game_state = "welcome"

# Font
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def reset_ball():
    ball.center = (WIDTH // 2, HEIGHT // 2)
    global ball_speed_x, ball_speed_y
    ball_speed_x = random.choice([-3, 3])
    ball_speed_y = -3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == "welcome" and event.key == pygame.K_SPACE:
                game_state = "playing"
            elif game_state == "game_over" and event.key == pygame.K_SPACE:
                game_state = "playing"
                score = 0
                lives = 3
                level = 1
                bricks = []
                for row in range(5):
                    for col in range(WIDTH // brick_width):
                        brick = pygame.Rect(col * brick_width, row * brick_height + 50, brick_width - 2, brick_height - 2)
                        bricks.append(brick)
                reset_ball()
            elif game_state == "game_over" and event.key == pygame.K_q:
                running = False

    if game_state == "playing":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed

        # Move the ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with walls
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed_x = -ball_speed_x
        if ball.top <= 0:
            ball_speed_y = -ball_speed_y

        # Ball collision with player
        if ball.colliderect(player):
            ball_speed_y = -ball_speed_y
            ball_speed_x += random.uniform(-0.5, 0.5)

        # Ball collision with bricks
        for brick in bricks[:]:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ball_speed_y = -ball_speed_y
                score += 10

        # Ball out of bounds
        if ball.bottom >= HEIGHT:
            lives -= 1
            if lives > 0:
                reset_ball()
            else:
                game_state = "game_over"

        # Level complete
        if len(bricks) == 0:
            level += 1
            ball_speed_x *= 1.2
            ball_speed_y *= 1.2
            player_speed += 1
            reset_ball()
            bricks = []
            for row in range(5):
                for col in range(WIDTH // brick_width):
                    brick = pygame.Rect(col * brick_width, row * brick_height + 50, brick_width - 2, brick_height - 2)
                    bricks.append(brick)

    # Drawing
    screen.fill(BLACK)

    if game_state == "welcome":
        draw_text("Welcome to Breakout!", WHITE, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text("Press SPACE to start", WHITE, WIDTH // 2, HEIGHT // 2 + 50)
    elif game_state == "playing":
        pygame.draw.rect(screen, PURPLE, player)
        pygame.draw.ellipse(screen, WHITE, ball)
        for brick in bricks:
            pygame.draw.rect(screen, RED, brick)
        draw_text(f"Score: {score}", WHITE, 70, 20)
        draw_text(f"Lives: {lives}", WHITE, WIDTH - 70, 20)
        draw_text(f"Level: {level}", WHITE, WIDTH // 2, 20)
    elif game_state == "game_over":
        draw_text("Game Over!", WHITE, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text(f"Final Score: {score}", WHITE, WIDTH // 2, HEIGHT // 2)
        draw_text("Press SPACE to play again", WHITE, WIDTH // 2, HEIGHT // 2 + 50)
        draw_text("Press Q to quit", WHITE, WIDTH // 2, HEIGHT // 2 + 100)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()