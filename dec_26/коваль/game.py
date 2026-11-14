import random
import pygame

# Ініціалізація
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пакмен")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

# Опис лабіринту (1 — стіна, 0 — прохід)
world_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

CELL_SIZE = 50  # Розмір однієї клітинки


# Базовий клас Sprite
class Sprite:

    def __init__(self, filename, x, y):
        self.image = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


# Клас гравця (Пакмен)
class Player(Sprite):

    def __init__(self, x, y):
        super().__init__("foni-papik-pro-oeca-p-kartinki-p (1).png", x, y)
        self.speed = CELL_SIZE
        self.score = 0
        self.game_over = False
        self.win = False

    def move(self, dx, dy):
        new_x = self.rect.x + dx * self.speed
        new_y = self.rect.y + dy * self.speed

        cell_x = new_x // CELL_SIZE
        cell_y = new_y // CELL_SIZE

        if 10 > cell_x >= 0 == world_map[cell_y][cell_x] and 0 <= cell_y < 10:
            self.rect.x = new_x
            self.rect.y = new_y


# Клас ворога (Привид) з уповільненням
class Enemy(Sprite):

    def __init__(self, x, y):
        super().__init__("png-transparent-pac-man-ghost-pa (1).png", x, y)
        self.speed = CELL_SIZE
        self.dx = 0
        self.dy = -CELL_SIZE
        self.move_timer = 0
        self.move_delay = 10  # Ворог робить крок кожні 3 ігрові кадри (чим більше число, тим повільніше)

    def update(self):
        self.move_timer += 1
        if self.move_timer < self.move_delay:
            return  # Чекаємо наступного кроку
        self.move_timer = 0

        next_x = self.rect.x + self.dx
        next_y = self.rect.y + self.dy
        c_x, c_y = next_x // CELL_SIZE, next_y // CELL_SIZE

        if 0 <= c_x < 10 and 0 <= c_y < 10 and world_map[c_y][c_x] == 0:
            self.rect.x = next_x
            self.rect.y = next_y
        else:
            directions = [
                (CELL_SIZE, 0),
                (-CELL_SIZE, 0),
                (0, CELL_SIZE),
                (0, -CELL_SIZE),
            ]
            self.dx, self.dy = random.choice(directions)



# Створюємо Пакмена та 3 вороги
player = Player(CELL_SIZE, CELL_SIZE)
enemies = [
    Enemy(CELL_SIZE * 8, CELL_SIZE * 8),
    Enemy(CELL_SIZE * 8, CELL_SIZE * 1),
    Enemy(CELL_SIZE * 1, CELL_SIZE * 8),
]

# Створення монет
coins = []
total_coins = 0

for row_idx, row in enumerate(world_map):
    for col_idx, cell in enumerate(row):
        if cell == 0:
            if not (row_idx == 1 and col_idx == 1):
                coins.append(Sprite("coin.png", col_idx * CELL_SIZE, row_idx * CELL_SIZE))
                total_coins += 1

running = True
while running:
    dx, dy = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # програмуємо рух гравця
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx, dy = -1, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = 1, 0
            elif event.key == pygame.K_UP:
                dx, dy = 0, -1
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, 1

    # програмуємо перевірку можливості руху
    if not player.game_over and not player.win:
        if dx != 0 or dy != 0:
            player.move(dx, dy)

        # Оновлення ворогів (тепер вони рухаються повільніше)
        for enemy in enemies:
            enemy.update()
            if player.rect.colliderect(enemy.rect):
                player.game_over = True

        # Збір монеток
        for coin in coins[:]:
            if player.rect.colliderect(coin.rect):
                coins.remove(coin)
                player.score += 1

        # Перемога
        if len(coins) == 0:
            player.win = True

    # Малювання
    screen.fill((200, 200, 200))

    for row_idx, row in enumerate(world_map):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(
                    screen,
                    (20, 20, 100),
                    (
                        col_idx * CELL_SIZE,
                        row_idx * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE,
                    ),
                )

    for coin in coins:
        coin.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    player.draw(screen)

    score_text = font.render(
        f"Зібрано: {player.score}/{total_coins}", True, (255, 255, 255)
    )
    screen.blit(score_text, (10, 10))

    if player.game_over:
        over_text = font.render("ПОРАЗКА!", True, (255, 50, 50))
        screen.blit(over_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
    elif player.win:
        win_text = font.render("ПЕРЕМОГА!", True, (50, 255, 50))
        screen.blit(win_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))

    pygame.display.flip()
    clock.tick(
        10
    )  # Швидкість гри залишається комфортною, а вороги рухаються ще рідше

pygame.quit()
