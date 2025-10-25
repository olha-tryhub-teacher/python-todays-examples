import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)

# ------------------ Клас кнопки ------------------
class Button:
    def __init__(self, x, y, w, h, text, color=BLUE, hover_color=GREEN):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.font = pygame.font.Font(None, 32)
        self.fn = None

    def draw(self, surf):
        # підсвічування при наведенні
        mx, my = pygame.mouse.get_pos()
        col = self.hover_color if self.rect.collidepoint(mx, my) else self.color
        pygame.draw.rect(surf, col, self.rect)
        text_surf = self.font.render(self.text, True, WHITE)
        surf.blit(text_surf, text_surf.get_rect(center=self.rect.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(event.pos) and self.fn:
                self.fn()

# ------------------ Функції переходів ------------------
def start_game():
    global game_part
    game_part = "game"

def win_game():
    global game_part
    game_part = "victory"

def lose_game():
    global game_part
    game_part = "gameover"

def back_menu():
    global game_part
    game_part = "menu"


def draw_menu(btn_list, text=None, color=RED):
    if text:
        font = pygame.font.Font(None, 50)
        text = font.render(text, True, color)
        screen.blit(text, (100, 100))
    for btn in btn_list:
        btn.draw(screen)
        btn.handle_event(e)

# ------------------ Кнопки ------------------
menu_buttons = [Button(100, 200, 300, 50, "Почати гру")]
menu_buttons[0].fn = start_game

game_buttons = [Button(100, 100, 300, 50, "Програш"), Button(100, 300, 300, 50, "Виграш")]
game_buttons[0].fn = lose_game
game_buttons[1].fn = win_game

victory_buttons = [Button(100, 300, 300, 50, "Повернутися в меню")]
victory_buttons[0].fn = back_menu

gameover_buttons = [Button(100, 300, 300, 50, "Повернутися в меню")]
gameover_buttons[0].fn = back_menu

# ------------------ Головний цикл ------------------
game_part = "menu"
running = True
while running:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # --- Відрисовка і обробка кнопок ---
    if game_part == "menu":
        draw_menu(menu_buttons)

    elif game_part == "game":
        draw_menu(game_buttons)

    elif game_part == "victory":
        draw_menu(menu_buttons, "Ви виграли!", GREEN)

    elif game_part == "gameover":
        draw_menu(menu_buttons, "Програш!", RED)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
