class Button:
    def __init__(self, x, y, width, height, text,
                 font_size=30, bg_color=BLUE,
                 hover_color=DARK_BLUE, text_color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont(None, font_size)
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
