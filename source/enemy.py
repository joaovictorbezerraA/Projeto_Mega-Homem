from collision import Collision


class Enemy(Collision):
    def __init__(self, x, y, width=48, height=48, health=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
