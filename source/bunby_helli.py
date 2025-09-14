import pygame
import global_var
from enemy import Enemy
from screen_config import Screen
from megaman import Megaman

pygame.init()

clock = pygame.time.Clock()


class Helicopter(Enemy):
    def __init__(self, x, y, width=13 * 3, height=15 * 3, health=4, damage=1):
        super().__init__(x, y, width, height, health, damage)
        self.x_coll = self.x
        self.y_coll = self.y
        self.sprites = [
            global_var.helicopter_sprites["Fly_1"],
            global_var.helicopter_sprites["Fly_2"],
        ]
        self.used_sprite = pygame.transform.scale_by(self.sprites[0], 3)
        self.anim_inx = 0

        self.screen_to_blit = Screen.display_screen

        self.collision = self.coll(0)

        self.direction = True

        self.attacking = False
        self.target = self.y

    def animation(self):
        cx = global_var.camera_x
        cy = global_var.camera_y
        if self.anim_inx == 7:
            self.anim_inx = 0
        if self.anim_inx == 3:
            self.used_sprite = self.sprites[1]
            self.used_sprite = pygame.transform.scale_by(self.used_sprite, 3)
            self.screen_to_blit.blit(self.used_sprite, (self.x - cx, self.y - cy))
        if self.anim_inx == 6:
            self.used_sprite = self.sprites[0]
            self.used_sprite = pygame.transform.scale_by(self.used_sprite, 3)
        pygame.draw.rect(self.screen_to_blit, "blue", self.collision)
        self.screen_to_blit.blit(self.used_sprite, (self.x - cx, self.y - cy))
        self.anim_inx += 1

    def move(self):
        cx = global_var.camera_x
        cy = global_var.camera_y
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
                self.collision = self.coll(0, 5, 10)

    def attack(self, mega_x, mega_y):
        if (
            mega_x - 100 < self.x < mega_x + 100
            and mega_y - 200 < self.y < mega_y + 200
        ):
            if not self.attacking:
                self.attacking = True
                self.target = 1

            if self.attacking and not self.direction and mega_x < self.x < mega_x + 100:
                self.down(mega_y)
            elif not self.direction and mega_x - 100 < self.x < mega_x:
                self.up()

            if self.direction and mega_x - 100 < self.x < mega_x:
                self.down(mega_y)
            elif self.direction and mega_x < self.x < mega_x + 100:
                self.up()

        print(self.target)

    def down(self, mega_y):
        if self.y - 7 > mega_y:
            self.y -= 7
        elif self.y + 7 < mega_y:
            self.y += 7
        self.y_coll = self.y

    def up(self):
        if self.y - 7 > self.target:
            self.y -= 7
        elif self.y + 7 < self.target:
            self.y += 7
        self.y_coll = self.y

    def check_col(self, mega_col):
        if mega_col.colliderect(self.collision):
            Megaman.take_damage(1)

    def run(self, mega_x, mega_y, mega_col):
        self.animation()
        self.move()
        self.attack(mega_x, mega_y)
        self.check_col(mega_col)
