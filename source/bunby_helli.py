import random
import pygame
import global_var
from enemy import Enemy
from screen_config import Screen
from megaman import Megaman
from random import randint

pygame.init()

clock = pygame.time.Clock()


class Helicopter(Enemy):
    def __init__(self, x=600, y=0, width=13 * 3, height=15 * 3, health=3, damage=1):
        super().__init__(
            x,
            y,
            width,
            height,
            health,
            damage,
        )
        self.x_coll = self.x
        self.y_coll = self.y
        self.sprites = [
            global_var.helicopter_sprites["Fly_1"],
            global_var.helicopter_sprites["Fly_2"],
        ]
        self.used_sprite = pygame.transform.scale_by(self.sprites[0].convert_alpha(), 3)

        self.collision = self.coll(0)

        self.direction = False

        self.attacking = False
        self.target = self.y

    def animation(self, bundy):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(bundy)):
            if bundy[i].anim_inx == 7:
                bundy[i].anim_inx = 0
            if bundy[i].anim_inx == 3:
                bundy[i].used_sprite = self.sprites[1].convert_alpha()
                bundy[i].used_sprite = pygame.transform.scale_by(
                    bundy[i].used_sprite, 3
                )
                bundy[i].screen_to_blit.blit(
                    bundy[i].used_sprite, (bundy[i].x - cx, bundy[i].y - cy)
                )
            if bundy[i].anim_inx == 6:
                bundy[i].used_sprite = self.sprites[0].convert_alpha()
                bundy[i].used_sprite = pygame.transform.scale_by(
                    bundy[i].used_sprite, 3
                )
            pygame.draw.rect(self.screen_to_blit, "blue", bundy[i].collision)
            bundy[i].screen_to_blit.blit(
                bundy[i].used_sprite, (bundy[i].x - cx, bundy[i].y - cy)
            )
            bundy[i].anim_inx += 1

    def move(self, enemies):
        cx = global_var.camera_x
        for i in range(len(enemies)):
            for j in range(100):
                if j * 10 == 0:
                    if enemies[i].x >= 720 + cx:
                        enemies[i].direction = False
                    if enemies[i].x <= -50 + cx:
                        enemies[i].direction = True
                    if enemies[i].direction:
                        enemies[i].x += 4
                        enemies[i].x_coll += 4
                    else:
                        enemies[i].x -= 4
                        enemies[i].x_coll -= 4
                    enemies[i].collision = enemies[i].coll(0, 5, 10)

    def attack(self, enemies, mega_x, mega_y):
        for i in range(len(enemies)):
            if (
                mega_x - 100 < enemies[i].x < mega_x + 100
                and mega_y - 180 < enemies[i].y < mega_y + 180
            ):
                if not enemies[i].attacking:
                    enemies[i].attacking = True
                    enemies[i].target = 1

                if (
                    enemies[i].attacking
                    and not enemies[i].direction
                    and mega_x < enemies[i].x < mega_x + 100
                ):
                    enemies[i].down(mega_y)
                elif not enemies[i].direction and mega_x - 100 < enemies[i].x < mega_x:
                    enemies[i].up()

                if enemies[i].direction and mega_x - 100 < enemies[i].x < mega_x:
                    enemies[i].down(mega_y)
                elif enemies[i].direction and mega_x < enemies[i].x < mega_x + 100:
                    enemies[i].up()

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

    def respawn_bunby(self, segment, rand_enemies):
        spawn_x = global_var.camera_x
        spawn_y = global_var.camera_y
        print(segment)
        if (
            segment == "Cutman_Stage_Segment_1"
            or segment == "Cutman_Stage_Segment_3"
            or segment == "Cutman_Stage_Segment_5"
        ) and len(rand_enemies) < 8:
            rand_enemies.append(Helicopter(720 + spawn_x, randint(100, 600) + spawn_y))
        return rand_enemies

    def delete(self, enemies):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            if (
                enemies[i].x - cx < -80
                or enemies[i].x - cx > 760
                or enemies[i].y - cy < -30
                or enemies[i].y - cy > 740
            ):
                enemies.remove(enemies[i])

    def run(self, enemies, mega_x, mega_y, mega_col, shoots):
        self.delete(enemies)
        self.animation(enemies)
        self.take_damage(enemies, shoots)
        self.move(enemies)
        self.attack(enemies, mega_x, mega_y)
        self.check_col(enemies, mega_col)
