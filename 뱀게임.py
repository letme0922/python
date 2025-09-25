import pygame
import random
import sys

# 초기화
pygame.init()

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 게임 설정
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLOCK_SIZE = 20
GAME_SPEED = 10  # 게임 속도 감소
APPLE_COUNT = 3  # 동시에 출현할 사과 개수

# 화면 설정
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('뱀 게임')
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + (x*BLOCK_SIZE)), (cur[1] + (y*BLOCK_SIZE)))
        
        if new[0] < 0 or new[0] >= WINDOW_WIDTH or \
           new[1] < 0 or new[1] >= WINDOW_HEIGHT or \
           new in self.positions[2:]:
            return True
        
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return False

    def reset(self):
        self.length = 1
        self.positions = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def render(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, 
                           (p[0], p[1], BLOCK_SIZE, BLOCK_SIZE))

class Apple:
    def __init__(self):
        self.positions = []  # 여러 개의 사과 위치를 저장할 리스트
        self.color = RED
        for _ in range(APPLE_COUNT):
            self.add_apple()

    def add_apple(self):
        new_position = (random.randint(0, (WINDOW_WIDTH-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE,
                       random.randint(0, (WINDOW_HEIGHT-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE)
        self.positions.append(new_position)

    def randomize_position(self):
        self.positions = []
        for _ in range(APPLE_COUNT):
            self.add_apple()

    def render(self, surface):
        for position in self.positions:
            pygame.draw.rect(surface, self.color,
                           (position[0], position[1], 
                            BLOCK_SIZE, BLOCK_SIZE))

def main():
    # 방향 설정
    global UP, DOWN, LEFT, RIGHT
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    snake = Snake()
    apple = Apple()
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != DOWN:
                    snake.direction = UP
                elif event.key == pygame.K_DOWN and snake.direction != UP:
                    snake.direction = DOWN
                elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                    snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                    snake.direction = RIGHT

        # 게임 오버 체크
        if snake.update():
            game_over_text = font.render('Game Over! Score: ' + str(snake.score), True, WHITE)
            screen.blit(game_over_text, (WINDOW_WIDTH//3, WINDOW_HEIGHT//2))
            pygame.display.update()
            pygame.time.wait(2000)  # 2초 대기
            running = False  # 게임 종료
            break

        # 사과를 먹었는지 체크
        head_pos = snake.get_head_position()
        for apple_pos in apple.positions[:]:  # 리스트 복사본으로 반복
            if head_pos == apple_pos:
                snake.length += 1
                snake.score += 1
                apple.positions.remove(apple_pos)
                apple.add_apple()  # 새로운 사과 추가

        screen.fill(BLACK)
        snake.render(screen)
        apple.render(screen)
        
        # 점수 표시
        score_text = font.render(f'Score: {snake.score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.update()
        clock.tick(GAME_SPEED)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()