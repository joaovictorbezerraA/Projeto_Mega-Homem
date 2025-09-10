import pygame
import global_var
from collision import Collision
from screen_config import Screen
import camera

pygame.init()

clock = pygame.time.Clock()

pixel_offset = 10
pixel_offset_y = 3

pygame.init()


class Megaman(Collision):
    def __init__(self, x, y, width=14 * 3, height=23 * 3):
        self.gravitty = 1
        self.speed = 8
        self.x = x
        self.y = y
        self.init_x = x
        self.init_y = y
        self.x_coll = x + pixel_offset
        self.y_coll = y - pixel_offset
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
        acceleration = self.gravitty * self.falling_counter
        if acceleration > 30:
            acceleration = 30
        self.y += acceleration
        self.y_coll = self.y + pixel_offset_y
        self.falling_counter += 0.5

    def colliding(self, mega_colision, collision):
        cx = camera.camera_x
        colliding = False
        for coll in collision:
            if mega_colision.colliderect(coll):
                self.onground = True
                self.acceleration = 0
                colliding = True
                mega_colision.bottom = coll.top
                self.y = mega_colision.top
                self.falling_counter = 0
                # elif self.y <= coll.bottom + 20:
                # self.onground = False
                # mega_colision.top = coll.bottom + 5
                # self.y = mega_colision.bottom

        if not colliding:
            self.onground = False
            self.falling()

    def coll_wall(self, mega_colision, collisions):
        cx = camera.camera_x
        for coll in collisions:
            if mega_colision.colliderect(coll):
                if mega_colision.left - cx > coll.right - 30 - cx:
                    self.x += self.speed
                    # mega_colision.left = coll.right
                    # self.x = mega_colision.right + cx
                elif mega_colision.right - cx < coll.left + 30 - cx:
                    self.x -= self.speed
                # bottom works fine
                self.x_coll = self.x
                print(mega_colision.left, coll.right - 30)

    def is_idle(self):
        if not (self.keys_pressed[pygame.K_d] or self.keys_pressed[pygame.K_a]) or (
            self.keys_pressed[pygame.K_a] and self.keys_pressed[pygame.K_d]
        ):
            self.moving = False
            self.animation_index = 0
            self.y_coll = self.y + pixel_offset_y
            self.x_coll = self.x + pixel_offset - camera.camera_x

    def move_right(self):
        if self.keys_pressed[pygame.K_d] and self.x - camera.camera_x < 720:
            self.moving = True
            self.left = True
            for _ in range(self.speed):
                self.x += 1
                self.x_coll = self.x + pixel_offset - camera.camera_x
        self.is_idle()

    def move_left(self):
        if self.keys_pressed[pygame.K_a] and self.x - camera.camera_x > -10:
            self.moving = True
            self.left = False
            for _ in range(self.speed):
                self.x -= 1
                self.x_coll = self.x + pixel_offset - camera.camera_x
        self.is_idle()

    def jump(self):
        if self.onground:
            self.jumping = True
            for i in range(20):
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

    def respawn(self):
        self.x = self.init_x
        self.y = self.init_y
        camera.camera_x = 0
