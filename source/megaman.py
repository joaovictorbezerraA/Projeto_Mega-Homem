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
        self.y_speed = 0

        self.keys_pressed = pygame.key.get_pressed()
        self.moving = False
        self.left = True

        self.animation_index = 0
        self.falling_counter = 1
        self.display_to_blit = Screen.display_screen

        self.onground = True
        self.on_ceiling = False
        self.jumping = False

        self.on_stair = False

        self.walk_sprites = [
            global_var.megaman_sprites["Megaman_Walk_1"],
            global_var.megaman_sprites["Megaman_Walk_2"],
            global_var.megaman_sprites["Megaman_Walk_3"],
            global_var.megaman_sprites["Megaman_Walk_2"],
        ]
        self.idle_sprites = [global_var.megaman_sprites["Mega_Stand_0"]]

        self.jump_sprites = [global_var.megaman_sprites["Mega_Jump"]]

        self.stair_sprite = [global_var.megaman_sprites["Megaman_Ladder_1"]]

        self.sprite = self.idle_sprites[0]

        self.display_to_blit = Screen.display_screen

    def falling(self):
        if not self.on_stair:
            self.y_speed = self.gravitty * self.falling_counter
            if self.y_speed > 30:
                self.y_speed = 30
            self.vertical_move(pixel_offset_y)
            self.falling_counter += 0.5

    def colliding(self, mega_colision, collision):
        cx = camera.camera_x
        colliding = False
        for coll in collision:
            if mega_colision.colliderect(coll):
                if not self.on_stair:
                    if (
                        mega_colision.bottom > coll.top - self.y_speed
                        and mega_colision.top < coll.top
                    ):
                        self.onground = True
                        self.y_speed = 0
                        colliding = True
                        mega_colision.bottom = coll.top
                        self.y = mega_colision.top
                        self.falling_counter = 0
                        break
                    if (
                        mega_colision.top < coll.bottom + self.y_speed
                        and mega_colision.bottom > coll.bottom
                    ):
                        self.jumping = False
                        mega_colision.top = coll.bottom
                        self.y_speed = 0
                        self.y = mega_colision.top
                        break
                else:
                    if mega_colision.top + 55 <= coll.top:
                        self.on_stair = False

        if not colliding:
            self.onground = False
            self.falling()

    def coll_wall(self, mega_colision, collisions):
        cx = camera.camera_x
        for coll in collisions:
            if mega_colision.colliderect(coll):
                if mega_colision.right - cx < coll.left + 30 - cx:
                    self.x -= self.speed
                elif mega_colision.left - cx > coll.right - 30 - cx:
                    self.x += self.speed
                    # mega_colision.left = coll.right
                    # self.x = mega_colision.right + cx
                # bottom works fine

    def on_stair_coll(self, events, mega_colision, stair_collisions):
        cx = camera.camera_x
        for coll in stair_collisions:
            if mega_colision.colliderect(coll):
                print(mega_colision.bottom, coll.top)
                if mega_colision.bottom <= coll.top + 10:
                    print("a")
                    self.on_stair = False
                for event in events:
                    if event.type == pygame.KEYDOWN and (
                        event.key == pygame.K_w or event.key == pygame.K_s
                    ):
                        if (
                            mega_colision.top < coll.bottom
                            or mega_colision.bottom > coll.top
                        ):
                            if mega_colision.bottom + 11 < coll.bottom:
                                self.y += 11
                            self.on_stair = True
                            mega_colision.right = coll.left + cx
                            self.x = coll.left + cx
                            self.x_coll = self.x - cx
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.on_stair = False

    def is_idle(self):
        if not (self.keys_pressed[pygame.K_d] or self.keys_pressed[pygame.K_a]) or (
            self.keys_pressed[pygame.K_a]
            and self.keys_pressed[pygame.K_d]
            or self.keys_pressed[pygame.K_w]
            or self.keys_pressed[pygame.K_s]
        ):
            self.moving = False
            self.animation_index = 0
            self.y_coll = self.y + pixel_offset_y
            self.x_coll = self.x + pixel_offset - camera.camera_x

    def move_right(self):
        if self.keys_pressed[pygame.K_d] and self.x - camera.camera_x < 720:
            self.left = True
            if not self.on_stair:
                self.moving = True
                for _ in range(self.speed):
                    self.x += 1
                    self.x_coll = self.x + pixel_offset - camera.camera_x
        self.is_idle()
        self.y_coll = self.y + 1

    def move_left(self):
        if self.keys_pressed[pygame.K_a] and self.x - camera.camera_x > -10:
            self.left = False
            if not self.on_stair:
                self.moving = True
                for _ in range(self.speed):
                    self.x -= 1
                    self.x_coll = self.x + pixel_offset - camera.camera_x
        self.is_idle()
        self.y_coll = self.y + 1

    def move_stair(self):
        cx = camera.camera_x
        if self.on_stair:
            if self.jumping:
                self.y_speed = 0
            if self.keys_pressed[pygame.K_w]:
                self.y_speed = -4
                self.moving = True
                self.vertical_move()
            if self.keys_pressed[pygame.K_s]:
                self.y_speed = 4
                self.moving = True
                self.vertical_move()
            self.x_coll = self.x - cx + 1

    def jump(self):
        if self.onground or self.on_stair:
            self.jumping = True
            for i in range(20):
                if i % 10 == 0 and not (self.on_ceiling or self.on_stair):
                    self.y_speed -= 1.5
                    self.vertical_move()

    def jumping_state(self):
        if self.onground or self.on_stair:
            self.jumping = False

        if self.jumping:
            for i in range(20):
                if i % 2:
                    self.y -= 1
                    self.y_coll = self.y

    def vertical_move(self, offset=0):
        self.y += self.y_speed
        self.y_coll = self.y + offset

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

    def stair_animation(self):
        if self.moving:
            self.sprite = self.stair_sprite[0]

    def animations(self):
        if self.animation_index == 39:
            self.animation_index = 0
        if self.on_stair:
            self.stair_animation()
        elif self.onground:
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
