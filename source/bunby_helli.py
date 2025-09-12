import pygame
import global_var
from enemy import Enemy
from screen_config import Screen
from megaman import Megaman
import camera

pygame.init()

clock = pygame.time.Clock()


class Helicopter(Enemy):
    def __init__(self, x, y, width=13 * 3, height=15 * 3, health=4):
        super().__init__(x, y, width, height, health)
        self.x_coll = self.x
        self.y_coll = self.y
        self.sprites = [
            global_var.helicopter_sprites["Fly_1"],
            global_var.helicopter_sprites["Fly_2"],
        ]
        self.used_sprite = pygame.transform.scale_by(self.sprites[0], 3)
        self.anim_inx = 0

        self.screen_to_blit = Screen.display_screen

        self.collision = pygame.Rect(self.x + 5, self.y + 10, self.width, self.height)

        self.direction = True

    def animation(self):
        cx = global_var.camera_x
        if self.anim_inx == 7:
            self.anim_inx = 0
        if self.anim_inx == 3:
            self.used_sprite = self.sprites[1]
            self.used_sprite = pygame.transform.scale_by(self.used_sprite, 3)
            self.screen_to_blit.blit(self.used_sprite, (self.x - cx, self.y))
        if self.anim_inx == 6:
            self.used_sprite = self.sprites[0]
            self.used_sprite = pygame.transform.scale_by(self.used_sprite, 3)
        pygame.draw.rect(self.screen_to_blit, "blue", self.collision)
        self.screen_to_blit.blit(self.used_sprite, (self.x - cx, self.y))
        self.anim_inx += 1

    def move(self):
        cx = global_var.camera_x
        for j in range(100):
            if j * 10 == 0:
                if self.x >= 720 + cx:
                    self.direction = False
                if self.x <= -50 + cx:
                    self.direction = True
                if self.direction:
                    self.x += 5
                    self.x_coll += 5
                else:
                    self.x -= 5
                    self.x_coll -= 5
                self.collision = pygame.Rect(
                    self.x_coll + 5 - cx, self.y_coll + 10, self.width, self.height
                )

    def run(self):
        self.animation()
        self.move()
