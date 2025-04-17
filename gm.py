import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball and paddle settings
BALL_SIZE = 25
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20

# Block settings
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 30
BLOCK_ROWS = 5
BLOCK_COLUMNS = 10
BLOCK_GAP = 0

# Wall thickness
WALL_THICKNESS = 10

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.Font(None, 40)

# Initialize paddle, ball, and blocks
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

ball_speed = [4, 4]
blocks = []

def create_blocks():
    global blocks
    x_offset = (WIDTH - (BLOCK_WIDTH * BLOCK_COLUMNS + BLOCK_GAP * (BLOCK_COLUMNS - 1))) // 2
    y_offset = 50
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLUMNS):
            block_x = x_offset + col * (BLOCK_WIDTH + BLOCK_GAP)
            block_y = y_offset + row * (BLOCK_HEIGHT + BLOCK_GAP)
            block = pygame.Rect(block_x, block_y, BLOCK_WIDTH, BLOCK_HEIGHT)
            blocks.append(block)

create_blocks()

# Game variables
score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddle with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= 5
    if keys[pygame.K_RIGHT]:
        paddle.x += 5
    paddle.x = max(WALL_THICKNESS, min(WIDTH - paddle.width - WALL_THICKNESS, paddle.x))

    # Move ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with walls
    if ball.left <= WALL_THICKNESS or ball.right >= WIDTH - WALL_THICKNESS:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= WALL_THICKNESS:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddle
    if paddle.colliderect(ball):
        ball_speed[1] = -ball_speed[1]
        ball.y = paddle.top - BALL_SIZE

    # Ball collision with blocks
    for block in blocks[:]:
        if block.colliderect(ball):
            ball_speed[1] = -ball_speed[1]
            blocks.remove(block)
            score += 1
            break

    # Reset ball if it falls below the screen
    if ball.top > HEIGHT:
        ball.x, ball.y = WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2
        ball_speed = [4, 4]
        score = 0

    # Drawing everything
    screen.fill(BLACK)

    # Draw walls
    pygame.draw.rect(screen, MAGENTA, (0, 0, WALL_THICKNESS, HEIGHT))
    pygame.draw.rect(screen, MAGENTA, (WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, HEIGHT))
    pygame.draw.rect(screen, MAGENTA, (0, 0, WIDTH, WALL_THICKNESS))

    # Draw paddle and ball
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, MAGENTA, block)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
