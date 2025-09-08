import pygame


class Collision:
    def __init__(self, object, x, y, width, height, colour="Blue"):
        self.object = object
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def coll(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
