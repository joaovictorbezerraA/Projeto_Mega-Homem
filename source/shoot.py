import pygame
import global_var
from screen_config import Screen
import camera


class Shoot:
    def __init__(self, x, y, width=6 * 3, height=6 * 3):
        self.shoot_x = x
        self.shoot_y = y
        self.width = width
        self.height = height
        self.shoot_amount = 0

        self.screen = Screen.display_screen
        self.enable_sprite = False
        self.buster_sprite = [global_var.megaman_sprites["Mega_Buster"]]

    def lemon_shoot(self, shoots):
        if self.shoot_amount < 3:
            self.shoot_amount += 1
        for i in range(len(shoots) - 1, -1, -1):
            shoots[i][0].enable_sprite = True

    def draw_sprite(self, shoots):
        for i in range(len(shoots) - 1, -1, -1):
            if shoots[i][0].enable_sprite:
                self.screen.blit(
                    pygame.transform.scale_by(self.buster_sprite[0], 3),
                    (
                        shoots[i][0].shoot_x - camera.camera_x,
                        shoots[i][0].shoot_y,
                    ),
                )

    def move_shoot(self, shoots):
        cx = camera.camera_x
        for i in range(len(shoots) - 1, -1, -1):
            if shoots[i][0].enable_sprite:
                for j in range(120):
                    if j % 10 == 0:
                        if -60 + cx < shoots[i][0].shoot_x < 720 + cx:
                            shoots[i][0].shoot_x += 1 * (1 - 2 * (not shoots[i][1]))
                        else:
                            shoots[i][0].enable_sprite = False
                            self.shoot_amount -= 1
                            shoots.remove(shoots[i])
                            break

    def run(self, shoots):
        self.draw_sprite(shoots)
        self.move_shoot(shoots)
