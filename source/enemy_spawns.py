from enemy import Blaster
from source import global_var

offset = 3
bw = 3 * 16
bh = 3 * 16


bl1_1 = Blaster(bw * 51 + offset, 5 * bh, False)
bl1_2 = Blaster(bw * 59 + offset, 8 * bh, False)

seg_1_en = [bl1_1, bl1_2]

bl2_1 = Blaster(bw * 61 + offset, -7 * bh, False)
bl2_2 = Blaster(bw * 57 + offset, -13 * bh, False)
bl2_3 = Blaster(bw * 55 + offset, -11 * bh, False)
bl2_4 = Blaster(bw * 55 + offset, -25 * bh, False)
bl2_5 = Blaster(bw * 52 - offset, -21 * bh, True)
bl2_6 = Blaster(bw * 59 + offset, -29 * bh, False)
bl2_7 = Blaster(bw * 55 - offset, -35 * bh, True)
bl2_8 = Blaster(bw * 59 + offset, -43 * bh, False)
bl2_9 = Blaster(bw * 57 + offset, -46 * bh, False)

seg_2_en = [
    bl1_1,
    bl1_2,
    bl2_1,
    bl2_2,
    bl2_3,
    bl2_4,
    bl2_5,
    bl2_6,
    bl2_7,
    bl2_8,
    bl2_9,
]

spawn = {"Cutman_Stage_Segment_1": seg_1_en, "Cutman_Stage_Segment_2": seg_2_en}


def spawn_enemies(segment, enemies):
    if segment == "Cutman_Stage_Segment_1":
        for enemy in seg_1_en:
            if enemy.can_respawn:
                enemies.append(enemy)
    elif segment == "Cutman_Stage_Segment_2":
        for enemy in seg_2_en:
            if enemy.can_respawn:
                enemies.append(enemy)
