import pygame
import global_var
from enemy import Enemy
from source import collision


class Blaster(Enemy):
    def __init__(self, x=0, y=0, width=9 * 3, height=16 * 3, health=1, damage=1):
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
            global_var.blaster_sprites["Blaster_0"],
            global_var.blaster_sprites["Blaster_Attack_0"],
            global_var.blaster_sprites["Blaster_Attack_1"],
            global_var.blaster_sprites["Blaster_Attack_2"],
        ]
        self.active_sprite = pygame.transform.scale_by(
            self.sprites[0].convert_alpha(), 3
        )
        self.reverse = False

        self.collision = self.coll()

        self.direction = False

        self.attacking = False

    def animation(self, enemies):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].anim_inx == 100:
                enemies[i].reverse = True

            if enemies[i].anim_inx == 0:
                enemies[i].reverse = False
            if enemies[i].anim_inx == 50:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[3].convert_alpha(), 3
                )
                enemies[i].collision = enemies[i].coll(0, -5 * 3)

            if enemies[i].anim_inx == 35:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[2].convert_alpha(), 3
                )

            elif enemies[i].anim_inx == 20:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[1].convert_alpha(), 3
                )

            elif enemies[i].anim_inx == 15:
                enemies[i].active_sprite = pygame.transform.scale_by(
                    enemies[i].sprites[0].convert_alpha(), 3
                )

            enemies[i].anim_inx += 1 - 2 * enemies[i].reverse
            enemies[i].screen_to_blit.blit(
                enemies[i].active_sprite, (enemies[i].x - cx, enemies[i].y - cy)
            )
            pygame.draw.rect(self.screen_to_blit, "red", enemies[i].collision)

    def check_health(self, enemies):
        for i in range(len(enemies) - 1, -1, -1):
            if enemies[i].health == 0:
                enemies.remove(enemies[i])
                enemies[i].can_respawn = True

    def in_screen(self, enemies):
        cx = global_var.camera_x
        cy = global_var.camera_y
        for i in range(len(enemies) - 1, -1, -1):
            if (enemies[i].x - cx < -80 or enemies[i].x - cx > 760) and (
                enemies[i].y - cy > -20 or enemies[i].y - cy < 760
            ):
                enemies[i].can_respawn = True
                enemies.remove(enemies[i])

    def run(self, enemies):
        for enemy in enemies:
            enemy.can_respawn = False
        self.in_screen(enemies)
        self.check_health(enemies)
        self.animation(enemies)
