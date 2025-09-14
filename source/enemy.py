from collision import Collision
from megaman import Megaman
from screen_config import Screen


class Enemy(Collision):
    def __init__(self, x, y, width=48, height=48, health=0, damage=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.damage = damage
        self.spawned = False
        self.anim_inx = 0
        self.screen_to_blit = Screen.display_screen

    def take_damage(self, enemies, shoots):
        for shoot in shoots:
            for enemy in enemies:
                if enemy.collision.colliderect(shoot[0].collision):
                    enemy.health -= 1
                    shoot[0].delete_shoot(shoots, shoot)
                    print("ouch ouch, seu merda")

    def check_col(self, enemies, mega_col):
        for i in range(len(enemies) - 1, -1, -1):
            if mega_col.colliderect(enemies[i].collision):
                Megaman.take_damage(1)
