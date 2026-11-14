import random
import pygame

# Ініціалізація
pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Аркадні гонки")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)


# Базовий клас Sprite (без transform, картинки вже правильного розміру)
class Sprite:

    def __init__(self, filename, x, y):
        self.image = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


# Клас гравця (Машина)
class Car(Sprite):

    def __init__(self, x, y):
        super().__init__("car.png", x, y)
        self.speed = 6
        self.score = 0
        self.game_over = False
        self.win = False

    def move(self):
        keys = pygame.key.get_pressed()
        # Рух вліво та вправо в межах дороги (наприклад, між x=50 та x=400)
        if keys[pygame.K_LEFT] and self.rect.x > 50:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - 100:
            self.rect.x += self.speed


# Клас рухомого об'єкта (Монетка або Ворог, що їде назустріч)
class RoadObject(Sprite):

    def __init__(self, filename, is_enemy=False):
        x = random.randint(50, WIDTH - 100)
        y = random.randint(-200, -50)  # Спавняться зверху за межами екрана
        super().__init__(filename, x, y)
        self.speed = 3
        self.is_enemy = is_enemy

    def update(self):
        self.rect.y += self.speed
        # Якщо об'єкт випав за нижній край екрана — спавнимо його зверху знову
        if self.rect.y > HEIGHT:
            self.respawn()

    def respawn(self):
        self.rect.y = random.randint(-200, -50)
        self.rect.x = random.randint(50, WIDTH - 100)


# Завантаження фону
bg = pygame.image.load("fon.jpg")
bg_y1 = 0
bg_y2 = -HEIGHT

# Створення гравця, монеток та ворогів
car = Car(225, 400)

# Створюємо кілька монеток та ворогів
objects = [
    RoadObject("coin.png", is_enemy=False),
    RoadObject("coin.png", is_enemy=False),
    RoadObject("enemy.png", is_enemy=True),
    RoadObject("enemy.png", is_enemy=True),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not car.game_over and not car.win:
        car.move()

        # Плавний рух фону (ефект дороги)
        bg_y1 += 2
        bg_y2 += 2
        if bg_y1 >= HEIGHT:
            bg_y1 = -HEIGHT
        if bg_y2 >= HEIGHT:
            bg_y2 = -HEIGHT

        # Оновлення об'єктів
        for obj in objects:
            obj.update()

            # Перевірка зіткнень з машиною
            if car.rect.colliderect(obj.rect):
                if obj.is_enemy:
                    car.game_over = True
                else:
                    car.score += 1
                    obj.respawn()
                    # Умова перемоги: зібрати 30 монеток
                    if car.score >= 30:
                        car.win = True

    # Малювання фону (дві картинки для безшовного циклу)
    screen.blit(bg, (0, bg_y1))
    screen.blit(bg, (0, bg_y2))

    # Малювання монет та ворогів
    for obj in objects:
        obj.draw(screen)

    # Малювання машини
    car.draw(screen)

    # Виведення рахунку
    score_text = font.render(f"Монети: {car.score}/30", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    # Екрани завершення гри
    if car.game_over:
        over_text = font.render("ПОРАЗКА!", True, (255, 50, 50))
        screen.blit(over_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))
    elif car.win:
        win_text = font.render("ПЕРЕМОГА!", True, (50, 255, 50))
        screen.blit(win_text, (WIDTH // 2 - 70, HEIGHT // 2 - 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
