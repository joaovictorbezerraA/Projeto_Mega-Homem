from screen_config import Screen
import global_var

right_b = False
left_b = False


def cam_move(
    segment,
    pos,
    speed_x,
    speed_y,
    right,
):
    meio = 360
    pos_relativa_x = pos[0] - global_var.camera_x
    pos_relativa_y = pos[1] - global_var.camera_y

    if segment == "Cutman_Stage_Segment_1":
        if right and pos_relativa_x > meio and pos[0] < 2700:
            global_var.camera_x += speed_x
        elif not right and pos_relativa_x < meio:
            if pos[0] > 340:
                global_var.camera_x -= speed_x
            if global_var.camera_x < 0:
                global_var.camera_x = 0
    elif segment == "Cutman_Stage_Segment_2":
        if pos_relativa_y < -30:
            global_var.camera_y -= 720
        if pos_relativa_y > 720:
            global_var.camera_y += 720
