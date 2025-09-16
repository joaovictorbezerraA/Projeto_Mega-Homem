import pygame
from random import randint

import global_var
from collision import Collision
from megaman import Megaman
from screen_config import Screen
from projectile import Projectile


class Enemy(Collision):
    def __init__(self, x, y, width=48, height=48, health=0, damage=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.damage = damage
        self.spawned = False
        self.anim_inx = 0
        self.screen_to_blit = Screen.display_screen
        self.can_respawn = True
        self.attacking = True

    def take_damage(self, enemies, shoots):
        for shoot in shoots:
            for enemy in enemies:
                if enemy.collision.colliderect(shoot[0].collision):
                    if enemy.attacking:
                        enemy.health -= 1
                    shoot[0].delete_shoot(shoots, shoot)

    def check_col(self, enemies, mega_col):
        for i in range(len(enemies) - 1, -1, -1):
            if mega_col.colliderect(enemies[i].collision):
                Megaman.take_damage(1)


class Blaster(Enemy, Projectile):
    def __init__(
        self, x=0, y=0, direction=True, width=9 * 3, height=16 * 3, health=1, damage=1
    ):
        super().__init__(
            x,
            y,
            width,
            height,
            health,
            damage,
        )
        self.direction = direction
        self.fv = 28 * self.direction  # flip value

        self.x_coll = self.x - 48 * self.direction
        self.y_coll = self.y

        self.sprites = [
            global_var.blaster_sprites["Blaster_0"],
            global_var.blaster_sprites["Blaster_Attack_0"],
            global_var.blaster_sprites["Blaster_Attack_1"],
            global_var.blaster_sprites["Blaster_Attack_2"],
            global_var.blaster_sprites["Blaster_Attack_1"],
            global_var.blaster_sprites["Blaster_Attack_0"],
        ]
        self.active_sprite = pygame.transform.scale_by(
            self.sprites[0].convert_alpha(), 3
        )

        self.collision = self.coll()

        self.attacking = False
        self.project = []

    def animation(self, enemies):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].anim_inx == 270:
                enemies[i].anim_inx = 0

            elif enemies[i].anim_inx == 245:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[0].convert_alpha(), 3
                )
                enemies[i].attacking = False

            elif enemies[i].anim_inx == 230:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[1].convert_alpha(), 3
                )

            elif enemies[i].anim_inx == 215:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[2].convert_alpha(), 3
                )

            elif enemies[i].anim_inx == 200:
                enemies[i].attack(enemies[i], 4)

            elif enemies[i].anim_inx == 150:
                enemies[i].attack(enemies[i], 3)

            elif enemies[i].anim_inx == 100:
                enemies[i].attack(enemies[i], 2)

            elif enemies[i].anim_inx == 50:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[3].convert_alpha(), 3
                )
                enemies[i].collision = enemies[i].coll(0, -5 * 3 + enemies[i].fv)
                enemies[i].attack(enemies[i], 1)

            elif enemies[i].anim_inx == 35:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[2].convert_alpha(), 3
                )

            elif enemies[i].anim_inx == 20:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[1].convert_alpha(), 3
                )
                enemies[i].attacking = True

            elif enemies[i].anim_inx == 15:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[0].convert_alpha(), 3
                )

            enemies[i].collision = enemies[i].coll(0, 20 + enemies[i].fv)
            enemies[i].anim_inx += 1
            enemies[i].screen_to_blit.blit(
                pygame.transform.flip(
                    enemies[i].active_sprite, enemies[i].direction, 0
                ),
                (enemies[i].x - cx, enemies[i].y - cy),
            )

    def check_health(self, enemies):
        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].health == 0:
                enemies[i].can_respawn = True
                enemies.remove(enemies[i])

    def in_screen(self, enemies):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            if (enemies[i].x - cx < -80 or enemies[i].x - cx > 760) or (
                enemies[i].y - cy < 0 or enemies[i].y - cy > 720
            ):
                enemies[i].can_respawn = True
                if enemies[i].health == 0:
                    enemies[i].health = 1
                enemies.remove(enemies[i])

    def attack(self, enemy, kind):
        proj = Projectile(enemy.direction, enemy.x, enemy.y, kind)
        enemy.project.append(proj)

    def run_proj(self, enemies, obj_bull, mega_col):
        for i in range(len(enemies) - 1, -1, -1):
            obj_bull.run_shoots(enemies[i].project, mega_col)

    def run(self, enemies, obj_bull, shoots, mega_col):
        for enemy in enemies:
            enemy.can_respawn = False
        self.in_screen(enemies)
        self.check_health(enemies)
        self.take_damage(enemies, shoots)
        self.animation(enemies)
        self.check_col(enemies, mega_col)
        self.run_proj(enemies, obj_bull, mega_col)


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
                or enemies[i].health == 0
            ):
                enemies.remove(enemies[i])

    def run(self, enemies, mega_x, mega_y, mega_col, shoots):
        self.delete(enemies)
        self.animation(enemies)
        self.take_damage(enemies, shoots)
        self.move(enemies)
        self.attack(enemies, mega_x, mega_y)
        self.check_col(enemies, mega_col)
