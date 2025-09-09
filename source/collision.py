import pygame


class Collision:
    def __init__(self, objeto, x, y, width, height):
        self.object = objeto
        self.x_coll = x
        self.y_coll = y
        self.width = width
        self.height = height

    def coll(self):
        return pygame.Rect(self.x_coll, self.y_coll, self.width, self.height)
