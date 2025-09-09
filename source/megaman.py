import pygame
import global_var
from collision import Collision
from screen_config import Screen
import camera

pygame.init()

clock = pygame.time.Clock()

pixel_offset = 6

pygame.init()


class Megaman(Collision):
    def __init__(self, x, y, width=17 * 3, height=23 * 3):
        self.gravitty = 1
        self.speed = 8
        self.x = x
        self.y = y
        self.x_coll = x + pixel_offset
        self.y_coll = y + pixel_offset
        self.width = width
        self.height = height

        self.keys_pressed = pygame.key.get_pressed()
        self.moving = False
        self.left = True

        self.animation_index = 0
        self.falling_counter = 1
        self.display_to_blit = Screen.display_screen

        self.onground = True
        self.jumping = False

        self.walk_sprites = [
            global_var.megaman_sprites["Megaman_Walk_1"],
            global_var.megaman_sprites["Megaman_Walk_2"],
            global_var.megaman_sprites["Megaman_Walk_3"],
            global_var.megaman_sprites["Megaman_Walk_2"],
        ]
        self.idle_sprites = [global_var.megaman_sprites["Mega_Stand_0"]]

        self.jump_sprites = [global_var.megaman_sprites["Mega_Jump"]]

        self.sprite = self.idle_sprites[0]

        self.display_to_blit = Screen.display_screen

    def falling(self):
        self.y += self.gravitty * self.falling_counter
        self.y_coll = self.y
        self.falling_counter += 0.5

    def colliding(self, mega_colision, collision):
        if mega_colision.colliderect(collision):
            self.onground = True
            mega_colision.bottom = collision.top
            self.y = mega_colision.top
            self.falling_counter = 0

        else:
            self.onground = False
            self.falling()

    def is_idle(self):
        if not (self.keys_pressed[pygame.K_d] or self.keys_pressed[pygame.K_a]) or (
            self.keys_pressed[pygame.K_a] and self.keys_pressed[pygame.K_d]
        ):
            self.moving = False
            self.animation_index = 0
            self.y_coll = self.y + pixel_offset
            self.x_coll = self.x + pixel_offset - camera.camera_x

    def move_right(self):
        if self.keys_pressed[pygame.K_d]:
            self.moving = True
            self.left = True
            for _ in range(self.speed):
                self.x += 1
                self.x_coll = self.x + pixel_offset - camera.camera_x
        self.is_idle()

    def move_left(self):
        if self.keys_pressed[pygame.K_a]:
            self.moving = True
            self.left = False
            self.x -= self.speed
            self.x_coll = self.x + pixel_offset - camera.camera_x
        self.is_idle()

    def jump(self):
        if self.onground:
            self.jumping = True
            for i in range(60):
                if i % 10 == 0:
                    self.y -= 1
                    self.y_coll = self.y

    def jumping_state(self):
        if self.onground:
            self.jumping = False

        if self.jumping:
            for i in range(20):
                if i % 2:
                    self.y -= 1
                    self.y_coll = self.y

    def walk_animation(self):
        if (
            self.animation_index == 0
            or self.animation_index == 10
            or self.animation_index == 20
            or self.animation_index == 30
        ):
            if self.left:
                self.sprite = pygame.transform.flip(
                    self.walk_sprites[self.animation_index // 10], 1, 0
                )
            else:
                self.sprite = self.walk_sprites[self.animation_index // 10]
        self.is_idle()
        self.animation_index += 1

    def idle_animation(self):
        if self.left:
            self.sprite = self.idle_sprites[0]
        else:
            self.sprite = pygame.transform.flip(self.idle_sprites[0], 1, 0)

    def falling_animation(self):
        if self.left:
            self.sprite = pygame.transform.flip(self.jump_sprites[0], 1, 0)
        else:
            self.sprite = self.jump_sprites[0]

    def animations(self):
        if self.animation_index == 39:
            self.animation_index = 0
        if self.onground:
            if self.moving:
                self.walk_animation()
            else:
                self.idle_animation()
        else:
            self.falling_animation()
        self.display_to_blit.blit(
            pygame.transform.scale_by(self.sprite, 3),
            (
                self.x - camera.camera_x,
                self.y - camera.camera_y,
            ),
        )
