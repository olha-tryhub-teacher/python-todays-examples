# ваш код
import random
import pygame

# Ініціалізація
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Вогонь і Вода")
clock = pygame.time.Clock()

# Використовуємо стандартний шрифт без SysFont
font = pygame.font.Font(None, 32)


# Звичайний базовий клас для об'єктів гри
class Sprite:

    def __init__(self, filename, x, y):
        self.image = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


# Клас гравця
class Player(Sprite):

    def __init__(self, filename, x, y, speed):
        super().__init__(filename, x, y)
        self.speed = speed
        self.score = 0

    def move(self, up, down, left, right):
        keys = pygame.key.get_pressed()
        if keys[left] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[right] and self.rect.x < WIDTH - 50:  # 50 - ширина персонажа
            self.rect.x += self.speed
        if keys[up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[down] and self.rect.y < HEIGHT - 50:  # 50 - висота персонажа
            self.rect.y += self.speed


# Клас предмета
class Item(Sprite):

    def __init__(self, filename):
        super().__init__(filename, 0, 0)
        self.respawn()

    def respawn(self):
        self.rect.x = random.randint(50, WIDTH - 50)
        self.rect.y = random.randint(50, HEIGHT - 50)


# Завантаження фону
bg = pygame.image.load("bg2.jpg")

# Створюємо гравців та предмети
fire_player = Player("hero-fire.png", 100, 250, 5)
water_player = Player("hero-water.png", 350, 250, 5)

fire_item = Item("fire.png")
water_item = Item("water.png")

running = True
winner_text = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Керування гравцями (Вогонь - WASD, Вода - Стрілки)
    fire_player.move(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    water_player.move(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

    # Збір предметів Вогнем
    if fire_player.rect.colliderect(fire_item.rect):
        fire_player.score += 1
        fire_item.respawn()
    if fire_player.rect.colliderect(water_item.rect):
        fire_player.score -= 1
        water_item.respawn()

    # Збір предметів Водою
    if water_player.rect.colliderect(water_item.rect):
        water_player.score += 1
        water_item.respawn()
    if water_player.rect.colliderect(fire_item.rect):
        water_player.score -= 1
        fire_item.respawn()

    # Умова перемоги (20 очок)
    if fire_player.score >= 20:
        winner_text = "Переміг Вогонь!"
        running = False
    elif water_player.score >= 20:
        winner_text = "Переміг Вода!"
        running = False

    # Малювання на екрані
    screen.blit(bg, (0, 0))
    fire_player.draw()
    water_player.draw()
    fire_item.draw()
    water_item.draw()

    # Виведення рахунку
    score_render = font.render(f"Вогонь: {fire_player.score} | Вода: {water_player.score}", True, (255, 255, 255))
    screen.blit(score_render, (80, 20))

    pygame.display.update()
    clock.tick(60)

# Виведення результату
print(winner_text)
pygame.quit()
