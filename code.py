import pygame

class Slider:
    def __init__(self, x, y, width, min_value=0, max_value=100,
                 knob_radius=15, # один рядок
                 track_color=(180, 180, 180), knob_color=(0, 120, 255), # один рядок
                 font=None, text_color=(0, 0, 0)): # один рядок
        self.rect = pygame.Rect(x, y, width, 5)  # доріжка
        self.knob_radius = knob_radius
        self.knob_x = x  # початкове положення повзунка
        self.dragging = False
        self.min_value = min_value
        self.max_value = max_value
        self.track_color = track_color
        self.knob_color = knob_color
        self.font = font
        self.text_color = text_color
