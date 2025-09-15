import sys
import pygame

sys.path.insert(1, "source")

from megaman import Megaman
from screen_config import Screen
from shoot import Shoot
from bunby_helli import Helicopter
from blaster import Blaster
from stage import Stage
import camera
import global_var

pygame.init()

screen = Screen()
clock = pygame.time.Clock()
event_timer = pygame.time.Clock()
timer = 5

running = True
soma = 0

mega = Megaman(
    45,
    528,
)
buster = Shoot(mega.x_coll + 30, mega.y_coll)
col_mega = mega.coll()
stage = Stage()
bundy = Helicopter(0, 0)
blaster = Blaster(600, 600)

shoots = []
random_enemies = []
enemies_bl = []
while running:
    screen.display_screen.fill("#00e8d8")
    stage.change_segment((mega.x, mega.y))
    stage.draw_stage()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mega.jump()
            if event.key == pygame.K_j and global_var.shoots < 3:
                buster_shoot = Shoot(mega.x, mega.y - 15)
                mega.shoot_direction = mega.left
                shoots.append((buster_shoot, mega.shoot_direction))
                buster.lemon_shoot(shoots)
            if event.key == pygame.K_p:
                if global_var.debug_mode is False:
                    global_var.debug_mode = True
                else:
                    global_var.debug_mode = False
            if event.key == pygame.K_o:
                if global_var.disable_bunby_spawn is False:
                    global_var.disable_bunby_spawn = True
                else:
                    global_var.disable_bunby_spawn = False

    col_mega = mega.coll(1)

    k = pygame.key.get_pressed()
    mega.keys_pressed = k

    pygame.draw.rect(screen.display_screen, "blue", col_mega)
    floor_col = stage.handle_coll()
    stair_col = stage.handle_stair_coll()
    mega.colliding(col_mega, floor_col)
    mega.on_stair_coll(events, col_mega, stair_col)

    segment = stage.selected_sprite

    mega.move_left()
    mega.move_right()
    mega.move_stair()
    mega.jumping_state()
    mega.animations()
    stage.spawn(segment, enemies_bl, mega.y)
    buster.run(shoots)
    blaster.run(enemies_bl)

    camera.cam_move(
        segment,
        [mega.x, mega.y],
        mega.speed,
        mega.left,
    )

    bundy.run(random_enemies, mega.x, mega.y, col_mega, shoots)

    if mega.y + global_var.camera_y > 1080:
        mega.respawn()

    pygame.display.flip()

    dt = clock.tick(60) / 1000
    timer -= dt

    if not global_var.disable_bunby_spawn:
        if timer <= 0:
            random_enemies = bundy.respawn_bunby(segment, random_enemies)
            timer = 3

quit()
