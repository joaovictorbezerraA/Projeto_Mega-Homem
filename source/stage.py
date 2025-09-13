import pygame
from screen_config import Screen
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
        self.sprites = [
            stage_sprites["Cutman_Stage_Segment_1"],
            stage_sprites["Cutman_Stage_Segment_2"],
            stage_sprites["Cutman_Stage_Segment_3"],
            stage_sprites["Cutman_Stage_Segment_4"],
        ]

        self.sprite_pos = {
            "Cutman_Stage_Segment_1": [0, 0],
            "Cutman_Stage_Segment_2": [2304, -3072],
            "Cutman_Stage_Segment_3": [2304, -3072],
            "Cutman_Stage_Segment_4": [1280 * 3, -3072 * 2],
        }

        self.selected_sprite = "Cutman_Stage_Segment_1"
        self.used_sprite = pygame.transform.scale_by(self.sprites[0], 3)

    def draw_stage(self):
        cx = global_var.camera_x
        cy = global_var.camera_y
        self.screen.blit(
            self.used_sprite,
            (
                self.sprite_pos[self.selected_sprite][0] - cx,
                self.sprite_pos[self.selected_sprite][1] - cy,
            ),
        )

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

    def change_segment(self, coordinates):
        on_seg_1 = coordinates[0] < 2690
        on_seg_2 = coordinates[0] >= 2690 or coordinates[1] < -30
        on_seg_3 = coordinates[0] >= 2496 and coordinates[1] <= -2490
        on_seg_4 = coordinates[0] >= 4410 or coordinates[1] <= -3120

        if on_seg_1:
            self.selected_sprite = "Cutman_Stage_Segment_1"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[0].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_1"
        if not on_seg_3 and on_seg_2:
            self.selected_sprite = "Cutman_Stage_Segment_2"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[1].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_2"
        if not on_seg_4 and on_seg_3:
            self.selected_sprite = "Cutman_Stage_Segment_3"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[2].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_3"
        if on_seg_4:
            self.selected_sprite = "Cutman_Stage_Segment_4"
            self.used_sprite = pygame.transform.scale_by(
                self.sprites[3].convert_alpha(), 3
            )
            self.selected_seg = "Cutman_Stage_Segment_4"
