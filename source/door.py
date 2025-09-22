import pygame
from collision import Collision
from screen_config import Screen
import global_var


class Door(Collision, Screen):
    def __init__(self, x, y, kind, width=48, height=12 * 16):
        self.x = x + 50
        self.x_coll = self.x
        self.y = y
        self.y_coll = self.y
        self.width = width
        self.height = height
        self.kind = kind

        self.collision = self.coll()
        self.sprite = global_var.stage_sprites["Door"]
        self.screen = self.display_screen

        self.already_open = False
        self.opening = False
        self.anim_inx = 0
        self.open_inx = 0

    def open(self, megaman):
        if not self.already_open and self.collision.colliderect(megaman):
            self.opening = True
            global_var.opening = True
            if self.kind:
                global_var.first_door_open = True
            else:
                global_var.second_door_open = True

    def draw_door(self):
        cx = global_var.camera_x
        cy = global_var.camera_y
        if not self.kind:
            for i in range(16 - self.open_inx):
                self.screen.blit(
                    pygame.transform.scale_by(self.sprite.convert_alpha(), 3),
                    (self.x - cx, self.y + 12 * i - cy),
                )
        elif self.kind:
            for i in range(2):
                for j in range(16 - self.open_inx):
                    self.screen.blit(
                        pygame.transform.scale_by(self.sprite.convert_alpha(), 3),
                        (self.x + 48 * i - cx, self.y + 12 * j - cy),
                    )
        self.collision = self.coll()

    def door_anim(self):
        for i in range(100):
            if not i % 10:
                self.anim_inx += 1
        if self.anim_inx == 300:
            self.open_inx += 4
            self.anim_inx = 0
        if self.open_inx == 16:
            self.opening = False
            global_var.opening = False
            self.already_open = True

    def run(self, megaman):
        self.draw_door()
        if self.opening:
            self.door_anim()
        self.open(megaman)
