import pygame

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


clock = pygame.time.Clock()
running = True

# створюємо шрифт
font = pygame.font.Font(None, 48)
font.set_italic(True)
font.set_bold(True)
# створення поверхні із текстом
text_image = font.render("Hello, world!", True, YELLOW)


while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # заливка екрана кольором
    screen.fill(BLUE)

    # відмальовка поверхні з текстом
    screen.blit(text_image, (150, 150))

    # оновлення дисплея
    pygame.display.flip()

    clock.tick(50)

pygame.quit()
