import pygame
import global_var
from enemy import Enemy
from projectile import Projectile


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
