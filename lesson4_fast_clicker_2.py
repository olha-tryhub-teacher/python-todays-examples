import pygame
import time
from random import randint

pygame.init()

'''створюємо вікно програми'''

back = (200, 255, 255)  # колір фону (background)
mw = pygame.display.set_mode((500, 500))  # Вікно програми (main window)
mw.fill(back)
clock = pygame.time.Clock()

'''клас прямокутник'''


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  # прямокутник
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):  # обведення існуючого прямокутника
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

    def collidepoint(self, x, y): # ⬅️
        return self.rect.collidepoint(x, y) # ⬅️


'''клас напис'''


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        self.outline(BLUE, 10)  # Додаємо малювання контуру
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


YELLOW = (255, 255, 0)
DARK_BLUE = (0, 0, 100)
BLUE = (80, 80, 255)
RED = (255, 0, 0) # ⬅️
GREEN = (0, 255, 51) # ⬅️

cards = []
num_cards = 4

x = 70

wait = 0

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text('CLICK', 14)
    cards.append(new_card)
    x = x + 100
game = True


while game:
    if wait == 0:
        # переносимо напис:
        wait = 20  # стільки тиків напис буде на одному місці
        click = randint(0, num_cards - 1)
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if i == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1

        # на кожному тику перевіряємо клік:
    for event in pygame.event.get(): # ⬅️
        if event.type == pygame.QUIT: # ❌
            game = False # ❌
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # ⬅️
            x, y = event.pos # ⬅️
            for i in range(num_cards): # ⬅️
                if cards[i].collidepoint(x, y): # ⬅️
                    if i == click: # ⬅️
                        cards[i].color(GREEN) # ⬅️
                    else: # ⬅️
                        cards[i].color(RED) # ⬅️
                    cards[i].fill() # ⬅️

    pygame.display.update()
    clock.tick(40)
