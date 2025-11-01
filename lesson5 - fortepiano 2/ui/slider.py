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

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            knob_rect = pygame.Rect(self.knob_x - self.knob_radius, # один рядок
                                    self.rect.y - self.knob_radius, # один рядок
                                    self.knob_radius * 2,
                                    self.knob_radius * 2)  # один рядок
            if knob_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.knob_x = max(self.rect.x, # один рядок
                              min(event.pos[0], # один рядок
                                  self.rect.x + self.rect.width)) # один рядок

    def draw(self, surface):
        # Доріжка
        pygame.draw.rect(surface, self.track_color, self.rect)
        # Повзунок
        pygame.draw.circle(surface, self.knob_color,  # один рядок
                           (self.knob_x, self.rect.y + self.rect.height // 2),  # один рядок
                           self.knob_radius)  # один рядок
        # Значення
        value = self.get_value()
        if self.font:
            text = self.font.render(f"Value: {value}", True, self.text_color)
            surface.blit(text, (self.rect.x, self.rect.y - 40))
        return value

    def get_value(self):
        ratio = (self.knob_x - self.rect.x) / self.rect.width
        return int(self.min_value + ratio * (self.max_value - self.min_value))
