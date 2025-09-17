import pygame
from screen_config import Screen


class Life_bar(Screen):
    def __init__(self, hp):
        self.hp = hp

    def display_health(self):
        pygame.draw.rect(
            self.screen_to_blit(),
            "black",
            (80, 23, 24, 168),
        )
        for i in range(self.hp):
            pygame.draw.rect(self.screen_to_blit(), "#F0DC9D", (83, 185 - 6 * i, 18, 3))
            pygame.draw.rect(self.screen_to_blit(), "#F1F3F5", (89, 185 - 6 * i, 6, 3))
