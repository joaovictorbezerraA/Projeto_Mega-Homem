import pygame
import camera
import copy
from list_coll import og_floor_col, og_stair_col, og_wall_col

bw = 3 * 16
bh = 3 * 16
of = 5
th = 10  # wall__collision_thickness


class Stage_collisions:
    def __init__(self):
        self.floor_collisions = copy.deepcopy(og_floor_col)
        self.stairs_collisions = copy.deepcopy(og_stair_col)
        self.wall_collisions = copy.deepcopy(og_wall_col)

    def update_coll(self):
        cx = camera.camera_x
        for i in range(len(self.floor_collisions)):
            self.floor_collisions[i][0] = og_floor_col[i][0] - cx

    def update_stair_coll(self):
        cx = camera.camera_x
        for i in range(len(self.stairs_collisions)):
            self.stairs_collisions[i][0] = og_stair_col[i][0] - cx

    def update_wall_coll(self):
        cx = camera.camera_x
        for i in range(len(self.wall_collisions)):
            self.wall_collisions[i][0] = og_wall_col[i][0] - cx
