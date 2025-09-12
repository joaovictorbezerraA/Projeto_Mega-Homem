import sys
import pygame

sys.path.insert(1, "source")

from megaman import Megaman
import soil
from screen_config import Screen
from shoot import Shoot
from glob_timer import Timer
from bunby_helli import Helicopter
from stage import Stage
import camera
import global_var

pygame.init()

screen = Screen()
clock = pygame.time.Clock()
event_timer = pygame.time.Clock()

running = True
soma = 0

mega = Megaman(
    45,
    528,
)
buster = Shoot(mega.x_coll + 30, mega.y_coll)
col_mega = mega.coll()
stage = Stage()

shoots = []
bunby = Helicopter(600, 100)
while running:
    Timer(clock)
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
            if event.key == pygame.K_j and buster.shoot_amount < 3:
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
                if global_var.wall_debug is False:
                    global_var.wall_debug = True
                else:
                    global_var.wall_debug = False

    col_mega = mega.coll()

    k = pygame.key.get_pressed()
    mega.keys_pressed = k

    pygame.draw.rect(screen.display_screen, "blue", col_mega)
    floor_col = stage.handle_coll()
    stair_col = stage.handle_stair_coll()
    mega.colliding(col_mega, floor_col)
    mega.on_stair_coll(events, col_mega, stair_col)

    mega.move_left()
    mega.move_right()
    mega.move_stair()
    mega.jumping_state()
    mega.animations()
    buster.run(shoots)
    bunby.run()

    segment = stage.selected_sprite

    camera.cam_move(
        segment,
        [mega.x, mega.y],
        mega.speed,
        mega.y_speed,
        mega.left,
    )
    # pos_relativa = mega.x - global_var.camera_x
    # meio_tela = screen.display_screen.get_width() / 2
    # if mega.left and pos_relativa > meio_tela and mega.x < 2700:
    # global_var.camera_x += mega.speed
    # elif not mega.left and pos_relativa < meio_tela:
    # if mega.x > 340:
    # global_var.camera_x -= mega.speed
    # if global_var.camera_x < 0:
    # global_var.camera_x = 0

    if mega.y + global_var.camera_y > 1080:
        mega.respawn()

    pygame.display.flip()

    dt = clock.tick(60)

quit()
