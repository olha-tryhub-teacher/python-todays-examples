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


class MyRect():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 200, 50)
        # створення активної та пасивної поверхней
        # створення поверхонь
        self.normal_surf = pygame.Surface(
            (self.rect.width, self.rect.height))
        self.normal_surf.fill(BLUE)

        self.hover_surf = pygame.Surface(
            (self.rect.width, self.rect.height))
        self.hover_surf.fill(RED)
        
        self.current_surf = self.normal_surf
        
    def update(self):
        # перевірка, чи курсор мишки над прямокутником
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.current_surf = self.hover_surf
        else:
            self.current_surf = self.normal_surf
            

    def draw(self, surface):
        # відмальовка потрібної поверхні
        surface.blit(self.current_surf, (self.rect.x, self.rect.y))


#######################################    
# об'єкт прямокутника, потрібно його створити
r = MyRect(100, 100)
running = True
clock = pygame.time.Clock()


while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # заливка екрана кольором
    screen.fill(YELLOW)
    # оновлення та відмальовка
    r.update()
    r.draw(screen)

    # оновлення дисплея
    pygame.display.flip()

    clock.tick(50)

pygame.quit()
