import pygame
import global_var


class Projectile:
    def __init__(self, name, direction, x, y):
        self.sprite = {
            global_var.pj_sprites["Blaster_proj"],
        }
        self.name = name

        self.x = x
        self.y = y
        self.x_coll = self.x
        self.y_coll = self.y

        self.direction = direction

    def move_shoot(self):
        pass
