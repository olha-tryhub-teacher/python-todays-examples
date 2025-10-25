        # створення поверхонь
        self.normal_surf = pygame.Surface(
            (self.rect.width, self.rect.height))
        self.normal_surf.fill(BLUE)

        self.hover_surf = pygame.Surface(
            (self.rect.width, self.rect.height))
        self.hover_surf.fill(RED)
        
        self.current_surf = self.normal_surf
