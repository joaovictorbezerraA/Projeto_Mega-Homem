import pygame
import camera
import copy

bw = 3 * 16
bh = 3 * 16
of = 5
th = 3  # wall__collision_thickness


class Floor_collisions:
    def __init__(self):
        self.b1 = pygame.Rect(385 + th, 480, 90 - th, 1)
        self.b3 = pygame.Rect(488 + th, 8 * bh, 87 - th, 5)

        self.f0 = pygame.Rect(0, 12 * bh, 36 * bw, bh)
        self.f1 = pygame.Rect(0, 6 * bh, 12 * bw, 10)
        self.f2 = pygame.Rect(14 * bw, 6 * bh, 14 * bw - of, bh)
        self.f3 = pygame.Rect(30 * bw, 6 * bh, 2 * bw, bh)
        self.f4 = pygame.Rect(33 * bw, 7 * bh, 2 * bw, bh)
        self.f5 = pygame.Rect(36 * bw, 10 * bh, 2 * bw, 10)
        self.f6 = pygame.Rect(38 * bw, 8 * bh, 4 * bw, 10)
        self.f7 = pygame.Rect(44 * bw, 9 * bh, 2 * bw, bh)
        self.f8 = pygame.Rect(46 * bw, 11 * bh, 2 * bw, bh)
        self.f9 = pygame.Rect(48 * bw, 12 * bh, 11 * bw, bh)
        self.f10 = pygame.Rect(54 * bw, 9 * bh, 3 * bw, bh)
        self.f11 = pygame.Rect(52 * bw, 9 * bh, bw, bh)
        self.f12 = pygame.Rect(59 * bw, 10 * bh, bw, bh)

        self.st0 = pygame.Rect(245, 288, 40, 300)

        self.w0 = pygame.Rect(8 * bw, 10 * bh, 2 * bw, 2 * bh)
        self.w1 = pygame.Rect(480, 385, 95, 195)

        self.original_floor_col = [
            self.b1,
            self.b3,
            self.f0,
            self.f1,
            self.f2,
            self.f3,
            self.f4,
            self.f5,
            self.f6,
            self.f7,
            self.f8,
            self.f9,
            self.f10,
            self.f11,
            self.f12,
        ]
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
