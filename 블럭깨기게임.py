import pygame
import sys

# 초기화
pygame.init()
WIDTH, HEIGHT = 600, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭깨기 게임")
CLOCK = pygame.time.Clock()

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 패들
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 15
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 10

# 공
BALL_RADIUS = 10
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = 5
ball_speed_y = -5

# 블럭
BLOCK_ROWS = 6
BLOCK_COLS = 10
BLOCK_WIDTH = WIDTH // BLOCK_COLS
BLOCK_HEIGHT = 30
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block_rect = pygame.Rect(col * BLOCK_WIDTH + 2, row * BLOCK_HEIGHT + 2, BLOCK_WIDTH - 4, BLOCK_HEIGHT - 4)
        blocks.append(block_rect)

font = pygame.font.SysFont("malgungothic", 36)
game_over = False
win = False

def draw():
    SCREEN.fill(BLACK)
    pygame.draw.rect(SCREEN, BLUE, paddle)
    pygame.draw.ellipse(SCREEN, WHITE, ball)
    for block in blocks:
        pygame.draw.rect(SCREEN, GREEN, block)
    if game_over:
        msg = "게임 오버!"
        text = font.render(msg, True, RED)
        SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    if win:
        msg = "클리어!"
        text = font.render(msg, True, BLUE)
        SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

def reset():
    global ball, ball_speed_x, ball_speed_y, paddle, blocks, game_over, win
    paddle.x = WIDTH // 2 - PADDLE_WIDTH // 2
    ball.x = WIDTH // 2 - BALL_RADIUS
    ball.y = HEIGHT // 2
    ball_speed_x = 5
    ball_speed_y = -5
    blocks = []
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLS):
            block_rect = pygame.Rect(col * BLOCK_WIDTH + 2, row * BLOCK_HEIGHT + 2, BLOCK_WIDTH - 4, BLOCK_HEIGHT - 4)
            blocks.append(block_rect)
    game_over = False
    win = False

# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if (game_over or win) and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reset()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    if not game_over and not win:
        # 공 이동
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # 벽 충돌
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed_x *= -1
        if ball.top <= 0:
            ball_speed_y *= -1

        # 패들 충돌
        if ball.colliderect(paddle):
            ball_speed_y *= -1
            # 패들 중앙에서 벗어날수록 x방향 속도 변화
            offset = (ball.centerx - paddle.centerx) / (PADDLE_WIDTH // 2)
            ball_speed_x = int(7 * offset)

        # 블럭 충돌
        hit_index = ball.collidelist(blocks)
        if hit_index != -1:
            hit_block = blocks.pop(hit_index)
            # 충돌 방향 판정
            if abs(ball.bottom - hit_block.top) < 10 and ball_speed_y > 0:
                ball_speed_y *= -1
            elif abs(ball.top - hit_block.bottom) < 10 and ball_speed_y < 0:
                ball_speed_y *= -1
            elif abs(ball.right - hit_block.left) < 10 and ball_speed_x > 0:
                ball_speed_x *= -1
            elif abs(ball.left - hit_block.right) < 10 and ball_speed_x < 0:
                ball_speed_x *= -1

        # 바닥에 닿으면 게임 오버
        if ball.bottom >= HEIGHT:
            game_over = True

        # 블럭 다 깨면 승리
        if not blocks:
            win = True

    draw()
    CLOCK.tick(60)