from image_loading import image_loader

main_sprite = "Mega_Stand_0"

megaman_sprites = image_loader("./sprites/Megaman_Sprites")

helicopter_sprites = image_loader(
    "./sprites/Enemy_Sprites/Helicopter_Helicopter_Sprites"
)

blaster_sprites = image_loader("./sprites/Enemy_Sprites/Blaster_Sprites")

stage_sprites = image_loader("./sprites/Stage")

pj_sprites = image_loader("./sprites/Enemy_Sprites/Projectiles_Sprites")

debug_mode = False
wall_debug = False

camera_x = 0
camera_y = 0
screen_ch = 0

spawn_timer = 5

shoots = 0

disable_bunby_spawn = False
