import pygame

pygame.mixer.init()

shoot = pygame.mixer.Sound("./audio/sfx/buster.wav")

damage = pygame.mixer.Sound("./audio/sfx/megaman_damage.wav")

death = pygame.mixer.Sound("./audio/sfx/death.wav")

enemy_fire = pygame.mixer.Sound("./audio/sfx/enemy_fire.wav")
enemy_fire.set_volume(0.3)

reflect_fire = pygame.mixer.Sound("./audio/sfx/buster_reflect.wav")

landing = pygame.mixer.Sound("./audio/sfx/big_eye_land.wav")
landing.set_volume(0.5)

door_open = pygame.mixer.Sound("./audio/sfx/door.wav")
