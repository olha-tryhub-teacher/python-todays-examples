from pygame import *
from settings import *
from sounds import load_sounds
from keys import draw_keys, create_key_rects
from ui.slider import Slider  # ⬅️

init()
screen = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption("Piano Game")

sounds = load_sounds(KEYS)
key_rects = create_key_rects(len(KEYS))
keys_list = list(KEYS.keys())
pressed_keys = set()

# Шрифт для слайдера ⬅️
font = font.SysFont(None, 55)

# Створюємо слайдер гучності ⬅️
volume_slider = Slider(50, 50, 200, font=font)

running = True
while running:
    screen.fill(WHITE)

    # клавіші
    draw_keys(screen, key_rects, pressed_keys)

    # Малюємо слайдер і отримуємо значення гучності ⬅️
    volume_value = volume_slider.draw(screen)
    volume = volume_value / 100  # переводимо в діапазон 0.0 - 1.0

    # Встановлюємо гучність для всіх звуків ⬅️
    for sound in sounds.values():
        sound.set_volume(volume)

    display.flip()

    for e in event.get():
        if e.type == QUIT:
            running = False

        # Слайдер ⬅️
        volume_slider.handle_event(e)

        # клавіатура
        if e.type == KEYDOWN:
            k = key.name(e.key)
            if k in sounds:
                sounds[k].play()
                idx = keys_list.index(k)
                pressed_keys.add(idx)

        if e.type == KEYUP:
            k = key.name(e.key)
            if k in sounds:
                idx = keys_list.index(k)
                if idx in pressed_keys:
                    pressed_keys.remove(idx)

        # миша по клавішах
        if e.type == MOUSEBUTTONDOWN:
            pos = e.pos
            for i, rect in enumerate(key_rects):
                if rect.collidepoint(pos):
                    sounds[keys_list[i]].play()
                    pressed_keys.add(i)

        if e.type == MOUSEBUTTONUP:
            pos = e.pos
            for i, rect in enumerate(key_rects):
                if i in pressed_keys and rect.collidepoint(pos):
                    pressed_keys.remove(i)
