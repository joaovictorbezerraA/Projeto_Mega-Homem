import pygame
from screen_config import Screen
from collision import Collision
from global_var import stage_sprites
from stage_coll import Stage_collisions
import camera
import global_var
from megaman import Megaman

pygame.init()


class Stage(Stage_collisions, Megaman):
    def __init__(self):
        super().__init__()
        self.screen = Screen.display_screen
        self.sprites = [stage_sprites["Cutman_Stage_Segment_1"]]

        self.used_sprite = pygame.transform.scale_by(self.sprites[0], 3)

    def draw_stage(self):
        cx = camera.camera_x
        self.screen.blit(self.used_sprite, (0 - cx, 0))

    def handle_coll(self):
        debug = global_var.debug_mode
        self.update_coll()
        for coll in self.floor_collisions:
            if debug:
                pygame.draw.rect(self.screen, "red", coll)
        return self.floor_collisions

    def handle_stair_coll(self):
        debug = global_var.debug_mode
        self.update_stair_coll()
        for coll in self.stairs_collisions:
            if debug:
                pygame.draw.rect(self.screen, "green", coll)
        return self.stairs_collisions

    def handle_wall_coll(self):
        debug = global_var.debug_mode
        self.update_wall_coll()
        for coll in self.wall_collisions:
            if debug:
                pygame.draw.rect(self.screen, "purple", coll)
        return self.wall_collisions
