import random
import pygame

# Ініціалізація
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Дино-раннер")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
FLOOR_Y = 350  # Висота підлоги


# Базовий клас для всіх ігрових об'єктів з картинками
class Sprite:

    def __init__(self, filename, x, y, width, height):
        ...

    def draw(self, surface, camera_x):
        # Зміщуємо малювання залежно від камери
        ...


# Клас гравця (Динозаврик)
class Player(Sprite):

    def __init__(self, x, y):
        ...

    def move(self):
        ...

        # Рух вліво (фон не рухається)
        ...

        # Рух вправо (штовхає світ вперед)
        ...

        # Стрибок
        ...

        # Гравітація
        ...

        # Зіткнення з підлогою
        ...


# Клас ворога (Скорпіон)
class Scorpion(Sprite):

    def __init__(self, x, y):
        ...

    def update(self):
        ...


# Клас перешкоди (Шипи)
class Spike(Sprite):

    def __init__(self, x, y):
        ...


# Завантаження фону
bg_image = ...
bg_width = ...

# Створюємо гравця, скорпіонів та шипи
player = ...

scorpions = ...

spikes = ...

camera_x = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not player.game_over:
        player.move()

        # Логіка камери: фон рухається вправо, коли гравець перетинає центр екрана
        ...

        # Оновлення та перевірка ворогів
        ...

        # Перевірка зіткнення з шипами
        ...

    # Малювання фону (робимо безшовне заповнення, щоб він повторювався при прокручуванні)
    ...

    # Малювання об'єктів світу
    ...

    # Виведення рахунку
    ...

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
