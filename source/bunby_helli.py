import pygame
from global_var import helicopter_sprites
from enemy import Enemy
from screen_config import Screen
from megaman import Megaman

pygame.init()

clock = pygame.time.Clock()


class Helicopter(Enemy):
    def __init__(self, position, width=13 * 3, height=15 * 3, health=4):
        super().__init__(position, width, height, health)
        self.sprites = [
            helicopter_sprites["Fly_1"],
            helicopter_sprites["Fly_2"],
        ]
        self.used_sprite = pygame.transform.scale_by(self.sprites[0], 3)
        self.anim_inx = 0

        self.screen_to_blit = Screen.display_screen
        self.x = position[0]
        self.y = position[1]

        self.collision = pygame.Rect(self.x + 5, self.y + 10, self.width, self.height)

        self.direction = True

    def animation(self):
        pygame.draw.rect(self.screen_to_blit, "blue", self.collision)
        if self.anim_inx == 7:
            self.anim_inx = 0
        if self.anim_inx == 3:
            self.used_sprite = self.sprites[1]
            self.used_sprite = pygame.transform.scale_by(self.used_sprite, 3)
            self.screen_to_blit.blit(self.used_sprite, self.position)
        if self.anim_inx == 6:
            self.used_sprite = self.sprites[0]
            self.used_sprite = pygame.transform.scale_by(self.used_sprite, 3)
        self.screen_to_blit.blit(self.used_sprite, self.position)
        self.anim_inx += 1

    def move(self):
        for j in range(100):
            if j * 10 == 0:
                if self.position[0] >= 720:
                    self.direction = False
                if self.position[0] <= -50:
                    self.direction = True
                if self.direction:
                    self.position[0] += 5
                    self.x += 5
                else:
                    self.position[0] -= 5
                    self.x -= 5
                self.collision = pygame.Rect(
                    self.x + 5, self.y + 10, self.width, self.height
                )

    def run(self):
        self.animation()
        self.move()
