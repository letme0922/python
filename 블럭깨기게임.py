import pygame
import random
import math

# 게임 초기화
pygame.init()

# 폰트 설정
try:
    # 윈도우의 기본 한글 폰트인 맑은 고딕 사용
    game_font = pygame.font.SysFont("malgun gothic", 24)
except:
    # 폰트가 없을 경우 기본 폰트 사용
    game_font = pygame.font.Font(None, 24)

# 화면 크기
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭깨기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# 아이템 클래스 추가
class Item:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.active = True
        self.speed = 3

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        if self.active:
            pygame.draw.rect(screen, PURPLE, self.rect)

# 총알 클래스 추가
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 10)
        self.speed = 7
        self.active = True

    def move(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.active = False

    def draw(self):
        if self.active:
            pygame.draw.rect(screen, YELLOW, self.rect)

# 블럭 클래스
class Block:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.active = True
        self.color = random.choice([RED, YELLOW, PURPLE, CYAN, ORANGE, GREEN])
        self.item_chance = 0.3  # 30% 확률로 아이템 드롭

    def draw(self):
        if self.active:
            pygame.draw.rect(screen, self.color, self.rect)

# 공 클래스
class Ball:
    def __init__(self):
        self.radius = 10
        self.x = WIDTH // 2
        self.y = HEIGHT - 50
        self.speed = 5
        self.dx = self.speed
        self.dy = -self.speed
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        # 벽 충돌 검사
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.dx *= -1
        if self.y <= self.radius:
            self.dy *= -1
        if self.y >= HEIGHT - self.radius:
            return True  # 게임 오버
        return False
    
    def bounce(self):
        self.dy *= -1
        
    def draw(self):
        pygame.draw.circle(screen, BLUE, (int(self.x), int(self.y)), self.radius)
        
    def check_collision(self, rect):
        # 공의 중심점
        center_x = self.x
        center_y = self.y
        
        # 사각형과의 충돌 검사
        closest_x = max(rect.left, min(center_x, rect.right))
        closest_y = max(rect.top, min(center_y, rect.bottom))
        
        distance = math.sqrt((center_x - closest_x) ** 2 + (center_y - closest_y) ** 2)
        
        return distance <= self.radius

# 플레이어 클래스
class Player:
    def __init__(self):
        # 패들의 폭을 300으로 변경 (기존 100의 3배)
        self.rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 30, 300, 20)

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

# 게임 루프
def main():
    clock = pygame.time.Clock()
    player = Player()
    ball = Ball()
    blocks = [Block(x, y, 50, 20) for x in range(0, WIDTH, 60) 
             for y in range(50, 200, 30)]
    running = True
    game_over = False
    
    # 아이템과 총알 리스트 추가
    items = []
    bullets = []
    has_gun = False  # 총알 발사 가능 여부

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and has_gun:
                    # 스페이스바로 총알 발사
                    bullets.append(Bullet(player.rect.centerx, player.rect.top))

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move(-7)
            if keys[pygame.K_RIGHT]:
                player.move(7)

            # 공 이동
            game_over = ball.move()

            # 아이템 이동
            for item in items[:]:
                item.move()
                if item.rect.colliderect(player.rect):
                    has_gun = True
                    items.remove(item)
                elif item.rect.y > HEIGHT:
                    items.remove(item)

            # 총알 이동
            for bullet in bullets[:]:
                bullet.move()
                if not bullet.active:
                    bullets.remove(bullet)

            # 패들과 공의 충돌
            if ball.check_collision(player.rect):
                ball.bounce()

            # 블럭과 공/총알의 충돌
            for block in blocks:
                if block.active:
                    # 공과 블럭 충돌
                    if ball.check_collision(block.rect):
                        block.active = False
                        ball.bounce()
                        # 아이템 생성
                        if random.random() < block.item_chance:
                            items.append(Item(block.rect.centerx, block.rect.centery))
                    
                    # 총알과 블럭 충돌
                    for bullet in bullets[:]:
                        if bullet.active and block.active and bullet.rect.colliderect(block.rect):
                            block.active = False
                            bullet.active = False
                            if random.random() < block.item_chance:
                                items.append(Item(block.rect.centerx, block.rect.centery))

        screen.fill(WHITE)
        player.draw()
        ball.draw()
        
        # 아이템, 총알, 블럭 그리기
        for item in items:
            item.draw()
        for bullet in bullets:
            bullet.draw()
        for block in blocks:
            block.draw()

        # 총알 보유 상태 표시
        if has_gun:
            text = "총알 사용 가능 (스페이스바)"
            text_surface = game_font.render(text, True, BLACK)
            screen.blit(text_surface, (10, HEIGHT - 30))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

