import pygame  # імпорт модуля pygame


# кольори у форматі RGB
YELLOW = (200, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# ініціалізація Pygame
pygame.init()
# створення вікна розміром 500x500 пікселів
screen = pygame.display.set_mode((500, 500))
# об'єкт для керування частотою кадрів
clock = pygame.time.Clock()
# змінна для керування основним циклом гри
running = True


# клас для об'єктів-спрайтів
class Sprite:
    def __init__(self, coord, color):
        self.image = pygame.Surface((100, 100))
        self.image.fill(color)
        self.rect = pygame.Rect(coord, (100, 100))
        self.dx = 5

    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > 500:
            self.dx = -5  # змінити напрямок руху вліво
        elif self.rect.left < 0:
            self.dx = 5   # змінити напрямок руху вправо


    def draw(self, surface):
        # відображення зображення (image) на екрані
        surface.blit(self.image, (self.rect.x, self.rect.y))


# створення списку ігрових об'єктів-спрайтів з різними кольорами та координатами
sprites = [
    Sprite((100, 100), RED),
    Sprite((200, 150), GREEN),
    Sprite((300, 250), BLUE)
]

# основний цикл гри
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(YELLOW)

    for sprite in sprites:
        sprite.update()  # оновити координати
        sprite.draw(screen)  # відобразити на екрані

    # оновлення зображення на екрані
    pygame.display.flip()


    # затримка для встановлення 50 кадрів/секунду
    clock.tick(50)


# вихід із Pygame
pygame.quit()
