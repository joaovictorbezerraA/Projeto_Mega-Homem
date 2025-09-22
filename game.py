import sys
import pygame

sys.path.insert(1, "source")

from tittle import tittle_screen
from megaman import Megaman
from screen_config import Screen
from shoot import Shoot
from enemy import Helicopter, Blaster, Octopus
from cutman import Cutman
from stage import Stage
from projectile import Projectile
import camera
import global_var

pygame.init()

screen = Screen()
clock = pygame.time.Clock()
event_timer = pygame.time.Clock()
timer = 5
octopus_timer = 2

running = True
soma = 0

mega = Megaman(
    45,
    400,
    # 6200,
    # -3333,
)
buster = Shoot(mega.x_coll + 30, mega.y_coll)
col_mega = mega.coll()
stage = Stage()
bundy = Helicopter(0, 0)
blaster = Blaster(600, 600)
octopus_bat = Octopus(16 * 3 * 14, 21 * 3 * 5, True, False)
bullets = Projectile(1, 0, 0, 0)
cut = Cutman(9813, -3333)

shoots = []
random_enemies = []
enemies_bl = []
enemies_oct_b = []

boss = []
rolling_cutter = []

tittle_screen(screen)
boss_enabled = 0

while running:
    screen.display_screen.fill("#00e8d8")
    stage.change_segment((mega.x, mega.y))
    stage.draw_stage()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not mega.stunned and event.key == pygame.K_z:
                mega.jump()
            if (
                not mega.stunned
                and mega.alive
                and not mega.stopped
                and event.key == pygame.K_x
                and global_var.shoots < 3
            ):
                buster_shoot = Shoot(mega.x - 130 * (not mega.left), mega.y - 15)
                mega.shoot_direction = mega.left
                shoots.append((buster_shoot, mega.shoot_direction))
                buster.lemon_shoot(shoots, mega)
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

    floor_col = stage.handle_coll()
    stair_col = stage.handle_stair_coll()
    mega.colliding(col_mega, floor_col)
    mega.on_stair_coll(events, col_mega, stair_col)

    segment = stage.selected_sprite

    if global_var.enable_boss:
        if len(boss) == 0:
            boss.append(cut)
        if cut.alive:
            cut.run(boss, rolling_cutter, floor_col, mega, col_mega, shoots)
        if len(rolling_cutter) == 1:
            cut.with_scissors = False
            rolling_cutter[0].run(cut, rolling_cutter, col_mega, mega)
        else:
            cut.with_scissors = True
    mega.run()
    if not mega.mid_transition:
        stage.spawn(segment, enemies_bl, "blaster")
        stage.spawn(segment, enemies_oct_b, "octopus")
        buster.run(shoots, mega)
        blaster.run(enemies_bl, bullets, shoots, col_mega, mega)
        octopus_bat.run(enemies_oct_b, floor_col, shoots, col_mega, octopus_timer, mega)
        mega.display_health()
        doors = stage.list_doors(segment)
        for door in doors:
            door.run(col_mega)
        bundy.run(random_enemies, mega.x, mega.y, col_mega, shoots, mega)
    mega.display_health()

    camera.cam_move(
        segment,
        [mega.x, mega.y],
        mega.speed,
        mega.left,
    )

    if mega.y - global_var.camera_y > 1080:
        mega.health = 0

    pygame.display.flip()

    dt = clock.tick(55) / 1000
    timer -= dt
    octopus_timer -= dt
    if octopus_timer <= 0:
        octopus_timer = 2

    if not global_var.disable_bunby_spawn:
        if timer <= 0:
            random_enemies = bundy.respawn_bunby(segment, random_enemies)
            timer = 3
    if mega.x >= 9622:
        global_var.enable_boss = True


quit()
