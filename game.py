import sys
import pygame

sys.path.insert(1, "source")

from megaman import Megaman
import soil
from screen_config import Screen
from shoot import Shoot
from glob_timer import Timer
from bunby_helli import Helicopter
import camera

pygame.init()

screen = Screen()
clock = pygame.time.Clock()
event_timer = pygame.time.Clock()

running = True

mega = Megaman(
    screen.display_screen.get_width() / 2,
    screen.display_screen.get_height() / 2,
)
buster = Shoot(mega.x_coll + 30, mega.y_coll)
col_mega = mega.coll()
floor = soil.Ground("Ground", 0, screen.display_screen.get_height() / 2 + 80, 1270, 100)
col_floor = floor.coll()

shoots = []
bunby = Helicopter(600, 100)
while running:
    Timer(clock)
    screen.display_screen.fill("black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mega.jump()
            if event.key == pygame.K_j and buster.shoot_amount < 3:
                buster_shoot = Shoot(mega.x, mega.y - 15)
                mega.shoot_direction = mega.left
                shoots.append((buster_shoot, mega.shoot_direction))
                buster.lemon_shoot(shoots)

    col_mega = mega.coll()

    k = pygame.key.get_pressed()
    mega.keys_pressed = k

    pygame.draw.rect(screen.display_screen, "red", col_floor)
    pygame.draw.rect(screen.display_screen, "blue", col_mega)
    mega.colliding(col_mega, col_floor)

    mega.move_left()
    mega.move_right()
    mega.jumping_state()
    mega.animations()
    buster.run(shoots)
    bunby.run()

    pos_relativa = mega.x - camera.camera_x
    meio_tela = screen.display_screen.get_width() / 2
    if mega.left and pos_relativa >= meio_tela:
        if pos_relativa == meio_tela:
            n = 8
        else:
            n = 9
        camera.camera_x += n
    elif not mega.left and pos_relativa <= meio_tela:
        if pos_relativa == meio_tela:
            n = 8
        else:
            n = 9
        camera.camera_x -= n

    pygame.display.flip()

    dt = clock.tick(50)

quit()
