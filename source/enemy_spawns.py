from blaster import Blaster

offset = 3
bw = 3 * 16
bh = 3 * 16


bl1 = Blaster(bw * 51 + offset, 5 * bh)
bl2 = Blaster(bw * 59 + offset, 8 * bh)
spawn = {"Cutman_Stage_Segment_1": [bl1, bl2]}
seg_1_en = [bl1, bl2]


def spawn_enemies(segment, enemies, mega_y):
    if segment == "Cutman_Stage_Segment_1":
        for enemy in seg_1_en:
            if enemy.can_respawn:
                enemies.append(enemy)
