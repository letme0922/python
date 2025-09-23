import pygame
import random

# 게임 설정
CELL_SIZE = 30
COLS = 10
ROWS = 20
WIDTH = CELL_SIZE * COLS
HEIGHT = CELL_SIZE * ROWS
FPS = 10

# 색상 정의
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# 테트로미노 도형
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1], [1, 1]],        # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]]   # Z
]

def rotate(shape):
    return [ [ shape[y][x] for y in range(len(shape)) ] for x in range(len(shape[0])-1, -1, -1) ]

class Tetromino:
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color

    def image(self):
        return self.shape

    def rotate(self):
        self.shape = rotate(self.shape)

def check_collision(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                if x + off_x < 0 or x + off_x >= COLS or y + off_y >= ROWS:
                    return True
                if y + off_y >= 0 and board[y + off_y][x + off_x]:
                    return True
    return False

def remove_row(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    lines_cleared = ROWS - len(new_board)
    for _ in range(lines_cleared):
        new_board.insert(0, [0 for _ in range(COLS)])
    return new_board, lines_cleared

def join_matrix(board, shape, offset, color):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell and y + off_y >= 0:
                board[y + off_y][x + off_x] = color

def new_tetromino():
    idx = random.randint(0, len(SHAPES) - 1)
    shape = SHAPES[idx]
    color = idx + 1
    return Tetromino(COLS // 2 - len(shape[0]) // 2, 0, shape, color)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    current = new_tetromino()
    game_over = False

    while not game_over:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(board, current.image(), (current.x - 1, current.y)):
                        current.x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(board, current.image(), (current.x + 1, current.y)):
                        current.x += 1
                elif event.key == pygame.K_DOWN:
                    if not check_collision(board, current.image(), (current.x, current.y + 1)):
                        current.y += 1
                elif event.key == pygame.K_UP:
                    rotated = rotate(current.image())
                    if not check_collision(board, rotated, (current.x, current.y)):
                        current.rotate()

        if not check_collision(board, current.image(), (current.x, current.y + 1)):
            current.y += 1
        else:
            join_matrix(board, current.image(), (current.x, current.y), current.color)
            board, _ = remove_row(board)
            current = new_tetromino()
            if check_collision(board, current.image(), (current.x, current.y)):
                game_over = True

        # 보드 그리기
        for y in range(ROWS):
            for x in range(COLS):
                if board[y][x]:
                    pygame.draw.rect(screen, COLORS[board[y][x] - 1], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, GRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

        # 현재 블록 그리기
        for y, row in enumerate(current.image()):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, COLORS[current.color - 1], ((current.x + x) * CELL_SIZE, (current.y + y) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, GRAY, ((current.x + x) * CELL_SIZE, (current.y + y) * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()