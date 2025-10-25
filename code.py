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


# ------------------ Клас ігрового спрайта ------------------
class GameSprite:
    def __init__(self, x, y, w, h, color, speed=0):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move_player(self, keys):
        """Рух гравця за стрілками"""
        speed = 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed
        if keys[pygame.K_UP]:
            self.rect.y -= speed
        if keys[pygame.K_DOWN]:
            self.rect.y += speed
        # межі екрана
        self.rect.clamp_ip(screen.get_rect())

    def collides(self, other):
        return self.rect.colliderect(other.rect)

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
    reset_game() # ⬅️⬅️⬅️
    if text:
        font = pygame.font.Font(None, 50)
        text = font.render(text, True, color)
        screen.blit(text, (100, 100))
    for btn in btn_list:
        btn.draw(screen)
        btn.handle_event(e)


# ------------------ Міні-гра ------------------
def reset_game():
    global player, goal, enemy
    player = GameSprite(215, 430, 70, 70, BLUE)
    goal = GameSprite(430, 0, 70, 70, GREEN)
    enemy = GameSprite(0, 0, 70, 70, RED)


def draw_game():
    goal.draw(screen)
    enemy.draw(screen)
    player.draw(screen)


def update_game(keys):
    player.move_player(keys)

    if player.collides(goal):
        win_game()
    elif player.collides(enemy):
        lose_game()

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
reset_game()

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
        keys = pygame.key.get_pressed()
        update_game(keys)
        draw_game()

    elif game_part == "victory":
        draw_menu(menu_buttons, "Ви виграли!", GREEN)

    elif game_part == "gameover":
        draw_menu(menu_buttons, "Програш!", RED)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
