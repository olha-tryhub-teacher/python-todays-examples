from pygame import *
from random import randint

init()
WIDTH = 1200
HEIGHT = 800
window = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()

player_rect = Rect(150, HEIGHT // 2 - 100, 100, 100)


def generate_pipes(count,pipe_width=140, gap=280, # один рядок
                   min_height=50, max_height=440, # один рядок
                   distance=650):
    pipes = []
    start_x = WIDTH
    for i in range(count):
        height = randint(min_height, max_height)
        top_pipe = Rect(start_x, 0, pipe_width, height)
        bottom_pipe = Rect(start_x, height + gap,  # один рядок
                           pipe_width, HEIGHT - (height + gap))
        pipes.extend([top_pipe, bottom_pipe])
        start_x += distance
    return pipes


pies = generate_pipes(150)
main_font = font.Font(None, 100)
score = 0
lose = False
y_vel = 2
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    window.fill('sky blue')
    draw.rect(window, 'red', player_rect)
    for pie in pies:
        if not lose:
            pie.x -= 8
        draw.rect(window, 'green', pie)
        if pie.x <= -100:
            pies.remove(pie)
            score += 0.5
        if player_rect.colliderect(pie):
            lose = True
    if len(pies) < 8:
        pies += generate_pipes(150)

    score_text = main_font.render(f'{int(score)}', 1, 'black')
    center_text = WIDTH // 2 - score_text.get_rect().w
    window.blit(score_text, (center_text, 40))

    keys = key.get_pressed()
    if keys[K_w] and not lose:
        player_rect.y -= 15
    else:
        player_rect.y += 6
    if keys[K_r] and lose:
        lose = False
        score = 0
        pies = generate_pipes(150)
        player_rect.y = HEIGHT // 2 - 100
        y_vel = 2
    if player_rect.y >= HEIGHT - player_rect.h: lose = True
    if lose:
        player_rect.y += y_vel
        y_vel *= 1.1

    display.update()
    clock.tick(60)
