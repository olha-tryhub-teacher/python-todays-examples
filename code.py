# підключення pygame
import pygame  # ⬅️

# кольори
YELLOW = (200, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# налаштування Pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
area1 = pygame.Surface((100,200))# ⬅️
area1.fill(GREEN)# ⬅️


clock = pygame.time.Clock()
running = True

# створення прямокутної поверхні


while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # заливка екрана кольором, відображення прямокутної поверхні
    screen.fill(BLUE)# ⬅️
    screen.blit(area1, (120, 50))# ⬅️

    # оновлення дисплея та обмеження частоти
    pygame.display.flip()   # ⬅️
    clock.tick()   # ⬅️


pygame.quit()
