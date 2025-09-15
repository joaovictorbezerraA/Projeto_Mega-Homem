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
        self.speed = 5
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
            if self.y_speed > 22:
                self.y_speed = 22
            self.vertical_move(pixel_offset_y)
            self.falling_counter += 0.38

    def colliding(self, mega_colision, collision):
        cx = global_var.camera_x
        cy = global_var.camera_y

        colliding = False
        for coll in collision:
            if mega_colision.colliderect(coll):
                if not self.on_stair and not global_var.screen_ch:
                    if (
                        mega_colision.left <= coll.right + self.speed + 10
                        and mega_colision.right > coll.right + self.speed
                        and mega_colision.bottom > coll.top + self.y_speed + 1
                        and mega_colision.top < coll.bottom - 1 - self.y_speed
                    ):
                        mega_colision.left = coll.right + 1
                        self.x = mega_colision.left - 13 + cx
                    elif (
                        mega_colision.right <= coll.left + self.speed + 10
                        and mega_colision.left < coll.left + self.speed
                        and mega_colision.bottom > coll.top + self.y_speed + 1
                        and mega_colision.top < coll.bottom - 1 - self.y_speed
                    ):
                        mega_colision.right = coll.left - 1
                        self.x = mega_colision.left - 13 + cx

                    elif (
                        mega_colision.bottom > coll.top - self.y_speed
                        and mega_colision.top < coll.top
                        and (
                            mega_colision.left >= coll.left
                            or mega_colision.right <= coll.right
                        )
                    ):
                        self.onground = True
                        self.y_speed = 0
                        colliding = True
                        mega_colision.bottom = coll.top
                        self.y = mega_colision.top + cy
                        self.falling_counter = 0
                    elif (
                        mega_colision.top < coll.bottom + self.y_speed
                        and mega_colision.bottom > coll.bottom
                        and (
                            mega_colision.left >= coll.left
                            or mega_colision.right <= coll.right
                        )
                    ):
                        self.jumping = False
                        mega_colision.top = coll.bottom
                        self.y = mega_colision.top + cy

                else:
                    if mega_colision.top + 55 <= coll.top:
                        self.x -= 8
                        self.on_stair = False

        if not colliding:
            self.onground = False
            self.falling()

    def on_stair_coll(self, events, mega_colision, stair_collisions):
        cx = global_var.camera_x
        for coll in stair_collisions:
            if mega_colision.colliderect(coll):
                if (
                    mega_colision.bottom <= coll.top + 10
                    or mega_colision.top >= coll.bottom - 20
                ):
                    self.on_stair = False
                for event in events:
                    if event.type == pygame.KEYDOWN and (
                        (
                            event.key == pygame.K_w
                            and mega_colision.bottom > coll.top + 1
                        )
                        or (
                            event.key == pygame.K_s
                            and mega_colision.bottom < coll.bottom + 1
                        )
                    ):
                        if (
                            mega_colision.top < coll.bottom
                            or mega_colision.bottom > coll.top
                        ):
                            if (
                                mega_colision.bottom + 11 < coll.bottom
                                and not self.on_stair
                            ):
                                self.y += 11
                            self.on_stair = True
                            mega_colision.right = coll.left + cx
                            self.x = coll.left + cx
                            self.x_coll = self.x - cx

    def is_idle(self):
        if not (self.keys_pressed[pygame.K_d] or self.keys_pressed[pygame.K_a]) or (
            self.keys_pressed[pygame.K_a] and self.keys_pressed[pygame.K_d]
        ):
            self.moving = False
            if not self.on_stair:
                self.animation_index = 0
            self.y_coll = self.y + pixel_offset_y - global_var.camera_y
            self.x_coll = self.x + pixel_offset - global_var.camera_x

    def move_right(self):
        cy = global_var.camera_y
        if self.keys_pressed[pygame.K_d] and self.x - global_var.camera_x < 720 - 58:
            self.left = True
            if not self.on_stair:
                self.moving = True
                for _ in range(self.speed):
                    self.x += 1
                    self.x_coll = self.x + pixel_offset - global_var.camera_x
        self.is_idle()
        self.y_coll = self.y + 1 - cy

    def move_left(self):
        cy = global_var.camera_y
        if self.keys_pressed[pygame.K_a] and self.x - global_var.camera_x > -10:
            self.left = False
            if not self.on_stair:
                self.moving = True
                for _ in range(self.speed):
                    self.x -= 1
                    self.x_coll = self.x + pixel_offset - global_var.camera_x + 3
        self.is_idle()
        self.y_coll = self.y + 1 - cy

    def move_stair(self):
        cx = global_var.camera_x
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
                    self.y_speed -= 3
                    self.vertical_move()

    def jumping_state(self):
        if self.onground or self.on_stair:
            self.jumping = False

        if self.jumping:
            cy = global_var.camera_y
            for i in range(20):
                if i % 2:
                    self.y -= 1
                    self.y_coll = self.y
            self.y_coll -= cy

    def vertical_move(self, offset=0):
        self.y += self.y_speed
        self.y_coll = self.y + offset - global_var.camera_y
        if global_var.screen_ch:
            self.handle_transition()

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
            if self.animation_index <= 10 or 20 < self.animation_index <= 30:
                self.sprite = self.stair_sprite[0]
            else:
                self.sprite = pygame.transform.flip(self.stair_sprite[0], 1, 0)
            self.animation_index += 1

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
            pygame.transform.scale_by(self.sprite.convert_alpha(), 3),
            (self.x - global_var.camera_x, self.y - global_var.camera_y),
        )

    def respawn(self):
        self.x = self.init_x
        self.y = self.init_y
        global_var.camera_x = 0

    def handle_transition(self):
        if self.y_speed <= 0:
            self.y -= 60
        else:
            self.y += 60

    @staticmethod
    def take_damage(damage):
        pass
