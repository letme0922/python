import pygame
import random

# 게임 설정
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLS, ROWS = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# 색상 정의
COLORS = [
    (0, 0, 0),      # 빈칸
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# 블록 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[2, 0, 0], [2, 2, 2]],  # J
    [[0, 0, 3], [3, 3, 3]],  # L
    [[4, 4], [4, 4]],        # O
    [[0, 5, 5], [5, 5, 0]],  # S
    [[0, 6, 0], [6, 6, 6]],  # T
    [[7, 7, 0], [0, 7, 7]]   # Z
]

class Tetromino:
    def __init__(self):
        self.type = random.randint(0, len(SHAPES) - 1)
        self.shape = SHAPES[self.type]
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + off_x < 0 or x + off_x >= COLS or y + off_y >= ROWS:
                    return True
                if board[y + off_y][x + off_x]:
                    return True
    return False

def merge(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + off_y][x + off_x] = cell

def clear_rows(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    cleared = ROWS - len(new_board)
    for _ in range(cleared):
        new_board.insert(0, [0 for _ in range(COLS)])
    return new_board, cleared

def draw_board(screen, board, tetromino):
    for y in range(ROWS):
        for x in range(COLS):
            color = COLORS[board[y][x]]
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    # Draw current tetromino
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen,
                    COLORS[cell],
                    ((tetromino.x + x) * BLOCK_SIZE, (tetromino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                    0
                )

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    tetromino = Tetromino()
    fall_time = 0
    fall_speed = 500
    score = 0

    running = True
    while running:
        screen.fill((0, 0, 0))
        fall_time += clock.get_rawtime()
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(board, tetromino.shape, (tetromino.x - 1, tetromino.y)):
                        tetromino.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(board, tetromino.shape, (tetromino.x + 1, tetromino.y)):
                        tetromino.x += 1
                elif event.key == pygame.K_DOWN:
                    if not check_collision(board, tetromino.shape, (tetromino.x, tetromino.y + 1)):
                        tetromino.y += 1
                elif event.key == pygame.K_UP:
                    old_shape = tetromino.shape
                    tetromino.rotate()
                    if check_collision(board, tetromino.shape, (tetromino.x, tetromino.y)):
                        tetromino.shape = old_shape

        if fall_time > fall_speed:
            if not check_collision(board, tetromino.shape, (tetromino.x, tetromino.y + 1)):
                tetromino.y += 1
            else:
                merge(board, tetromino.shape, (tetromino.x, tetromino.y))
                board, cleared = clear_rows(board)
                score += cleared * 100
                tetromino = Tetromino()
                if check_collision(board, tetromino.shape, (tetromino.x, tetromino.y)):
                    running = False  # 게임 오버
            fall_time = 0

        draw_board(screen, board, tetromino)
        pygame.display.flip()

    print("Game Over! Score:", score)
    pygame.quit()

if __name__ == "__main__":
    main()