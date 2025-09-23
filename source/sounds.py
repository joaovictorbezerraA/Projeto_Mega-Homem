import pygame

pygame.mixer.init()

shoot = pygame.mixer.Sound("./audio/sfx/buster.wav")

damage = pygame.mixer.Sound("./audio/sfx/megaman_damage.wav")

death = pygame.mixer.Sound("./audio/sfx/death.wav")

enemy_fire = pygame.mixer.Sound("./audio/sfx/enemy_fire.wav")
