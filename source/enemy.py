from collision import Collision


class Enemy(Collision):
    def __init__(self, position=[0, 0], width=48, height=48, health=0):
        self.position = position
        self.width = width
        self.height = height
        self.health = health
