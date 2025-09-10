import pygame
import camera
import copy


class Floor_collisions:
    def __init__(self):
        self.b1 = pygame.Rect(385, 480, 90, 5)
        self.b3 = pygame.Rect(488, 380, 87, 5)
        self.f0 = pygame.Rect(0, 575, 1730, 10)
        self.f1 = pygame.Rect(0, 288, 574, 10)

        self.st0 = pygame.Rect(245, 288, 40, 300)

        self.w0 = pygame.Rect(380, 490, 100, 80)
        self.w1 = pygame.Rect(480, 385, 95, 195)

        self.original_floor_col = [self.b1, self.b3, self.f0, self.f1]
        self.original_stair_col = [self.st0]
        self.original_wall_col = [self.w0, self.w1]

        self.floor_collisions = copy.deepcopy(self.original_floor_col)
        self.stairs_collisions = copy.deepcopy(self.original_stair_col)
        self.wall_collisions = copy.deepcopy(self.original_wall_col)

    def update_coll(self):
        cx = camera.camera_x
        for i in range(len(self.floor_collisions)):
            self.floor_collisions[i][0] = self.original_floor_col[i][0] - cx

    def update_stair_coll(self):
        cx = camera.camera_x
        for i in range(len(self.stairs_collisions)):
            self.stairs_collisions[i][0] = self.original_stair_col[i][0] - cx

    def update_wall_coll(self):
        cx = camera.camera_x
        for i in range(len(self.wall_collisions)):
            self.wall_collisions[i][0] = self.original_wall_col[i][0] - cx
