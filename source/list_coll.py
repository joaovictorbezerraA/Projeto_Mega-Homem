import pygame

bw = 3 * 16
bh = 3 * 16
of = 5
th = 3  # wall__collision_thickness

selected_seg = "Cutman_Stage_Segment_1"

b0 = pygame.Rect(8 * bw, 10 * bh, 2 * bw, 2 * bh)
b1 = pygame.Rect(8 * bw, 4 * bh, 2 * bw, 2 * bh)
b2 = pygame.Rect(24 * bw, 4 * bh, 2 * bw, 2 * bh)
b3 = pygame.Rect(24 * bw, 10 * bh, 2 * bw, 2 * bh)
b4 = pygame.Rect(26 * bw, 8 * bh, 2 * bw, 4 * bh)
b5 = pygame.Rect(40 * bw, 6 * bh, 2 * bw, 4 * bh)


f0 = pygame.Rect(0, 12 * bh, 36 * bw, bh)
f1 = pygame.Rect(0, 6 * bh, 12 * bw, bh)
f2 = pygame.Rect(14 * bw, 6 * bh, 14 * bw, bh)
f3 = pygame.Rect(30 * bw, 6 * bh, 2 * bw, bh)
f4 = pygame.Rect(33 * bw, 7 * bh, 2 * bw, bh)
f5 = pygame.Rect(36 * bw, 10 * bh, 2 * bw, bh)
f6 = pygame.Rect(38 * bw, 8 * bh, 4 * bw, 9 * bh)
f7 = pygame.Rect(44 * bw, 9 * bh, 2 * bw, 8 * bh)
f8 = pygame.Rect(46 * bw, 11 * bh, 2 * bw, bh)
f9 = pygame.Rect(48 * bw, 12 * bh, 11 * bw, bh)
f10 = pygame.Rect(54 * bw, 9 * bh, 3 * bw, bh)
f11 = pygame.Rect(52 * bw, 5 * bh, bw, 5 * bh)
f12 = pygame.Rect(59 * bw, 10 * bh, bw, 2 * bh)
f13 = pygame.Rect(52 * bw, 4 * bh, 3 * bw, bh)
f14 = pygame.Rect(57 * bw, 4 * bh, 5 * bw, 2 * bh)

st0 = pygame.Rect(5 * bw, 6 * bh - 1, bw, 6 * bh)
st1 = pygame.Rect(10 * bw, 6 * bh - 1, bw, 2 * bh)
st2 = pygame.Rect(21 * bw, 6 * bh - 1, bw, 6 * bh)
st3 = pygame.Rect(53 * bw, 4 * bh - 1, bw, 6 * bh)
st4 = pygame.Rect(61 * bw, -3 * bh, bw, 7 * bh)

w0 = pygame.Rect(10 * bw, 8 * bh, 2 * bw + 5, 4 * bh)
w1 = pygame.Rect(0, 6 * bh, 12 * bw + 10, bh)
w2 = pygame.Rect(54 * bw, 5 * bh, bw, bh)
w3 = pygame.Rect(60 * bw, 6 * bh, bw, 4 * bh)
w4 = pygame.Rect(60 * bw, 0, bw, 2 * bh)
w5 = pygame.Rect(62 * bw, 0, bw, 4 * bh)
w6 = pygame.Rect(36 * bw, 10 * bh, 2 * bw, 2 * bh)

og_floor_col = [
    b0,
    b1,
    b2,
    b3,
    b4,
    b5,
    f0,
    f1,
    f2,
    f3,
    f4,
    f5,
    f6,
    f7,
    f8,
    f9,
    f10,
    f11,
    f12,
    f13,
    f14,
    w0,
    w1,
    w2,
    w3,
    w4,
    w5,
    w6,
]

og_stair_col = [
    st0,
    st1,
    st2,
    st3,
    st4,
]

f2_0 = pygame.Rect(48 * bw, 12 * bh, 11 * bw, bh)
f2_1 = pygame.Rect(54 * bw, 9 * bh, 3 * bw, bh)
f2_2 = pygame.Rect(59 * bw, 10 * bh, bw, 2 * bh)
f2_3 = pygame.Rect(57 * bw, 4 * bh, 5 * bw, 2 * bh)
f2_4 = pygame.Rect(60 * bw, -3 * bh, 2 * bw, bh)
f2_5 = pygame.Rect(48 * bw, -3 * bh, 10 * bw, 3 * bh)
f2_6 = pygame.Rect(50 * bw, -8 * bh, 2 * bw, bh)
f2_7 = pygame.Rect(54 * bw, -9 * bh, 8 * bw, 2 * bh)
f2_8 = pygame.Rect(56 * bw, -11 * bh, 6 * bw, 2 * bh)
f2_9 = pygame.Rect(58 * bw, -13 * bh, 4 * bw, 2 * bh)
f2_10 = pygame.Rect(56 * bw, -19 * bh, 6 * bw, bh)
f2_11 = pygame.Rect(56 * bw, -19 * bh, 5 * bw, 3 * bh)
f2_12 = pygame.Rect(50 * bw, -19 * bh, 3 * bw, 3 * bh)
f2_13 = pygame.Rect(50 * bw, -21 * bh, 2 * bw, 2 * bh)
f2_14 = pygame.Rect(50 * bw, -27 * bh, 2 * bw, bh)
f2_15 = pygame.Rect(51 * bw, -26 * bh, bw, bh)
f2_16 = pygame.Rect(56 * bw, -25 * bh, bw, 2 * bh)
f2_17 = pygame.Rect(57 * bw, -25 * bh, bw, bh)
f2_18 = pygame.Rect(58 * bw, -27 * bh, 2 * bw, 4 * bh)
f2_19 = pygame.Rect(60 * bw, -29 * bh, 2 * bw, 6 * bh)
f2_20 = pygame.Rect(57 * bw, -35 * bh, 4 * bw, 3 * bh)
f2_21 = pygame.Rect(61 * bw, -35 * bh, bw, bh)
f2_22 = pygame.Rect(51 * bw, -35 * bh, 4 * bw, 3 * bh)
f2_23 = pygame.Rect(51 * bw, -40 * bh, 9 * bw, bh)
f2_24 = pygame.Rect(51 * bw, -43 * bh, 5 * bw, bh)
f2_25 = pygame.Rect(51 * bw, -51 * bh, bw, bh)
f2_26 = pygame.Rect(52 * bw, -51 * bh, 8 * bw, 3 * bh)


w2_1 = pygame.Rect(60 * bw, 6 * bh, bw, 4 * bh)
w2_2 = pygame.Rect(60 * bw, -2 * bh, bw, 4 * bh)
w2_3 = pygame.Rect(62 * bw, 0, bw, 4 * bh)
w2_4 = pygame.Rect(36 * bw, 10 * bh, 2 * bw, 2 * bh)
w2_5 = pygame.Rect(62 * bw, -44 * bh, 2 * bw, 50 * bh)
w2_6 = pygame.Rect(51 * bw, -7 * bh, bw, bh)
w2_7 = pygame.Rect(60 * bw, -44 * bh, 2 * bw, 6 * bh)
w2_8 = pygame.Rect(54 * bw, -48 * bh, 2 * bw, bh)
w2_9 = pygame.Rect(55 * bw, -47 * bh, 3 * bw, bh)
w2_10 = pygame.Rect(58 * bw, -46 * bh, 2 * bw, bh)
w2_11 = pygame.Rect(59 * bw, -45 * bh, 2 * bw, bh)

st2_0 = pygame.Rect(61 * bw, -3 * bh - 1, bw, 7 * bh)
st2_1 = pygame.Rect(50 * bw, -8 * bh - 1, bw, 5 * bh)
st2_2 = pygame.Rect(61 * bw, -19 * bh - 1, bw, 6 * bh)
st2_3 = pygame.Rect(57 * bw, -25 * bh - 1, bw, 6 * bh)
st2_4 = pygame.Rect(50 * bw, -27 * bh - 1, bw, 6 * bh)
st2_5 = pygame.Rect(61 * bw, -35 * bh - 1, bw, 6 * bh)
st2_6 = pygame.Rect(52 * bw, -40 * bh - 1, bw, 5 * bh)
st2_7 = pygame.Rect(51 * bw, -51 * bh - 1, bw, 8 * bh)

og_floor_col_2 = [
    f2_0,
    f2_1,
    f2_2,
    f2_3,
    f2_4,
    f2_5,
    f2_6,
    f2_7,
    f2_8,
    f2_9,
    f2_10,
    f2_11,
    f2_12,
    f2_13,
    f2_14,
    f2_15,
    f2_16,
    f2_17,
    f2_18,
    f2_19,
    f2_20,
    f2_21,
    f2_22,
    f2_23,
    f2_24,
    f2_25,
    f2_26,
    w2_1,
    w2_2,
    w2_3,
    w2_4,
    w2_5,
    w2_6,
    w2_7,
    w2_8,
    w2_9,
    w2_10,
    w2_11,
]

og_stair_col_2 = [
    st2_0,
    st2_1,
    st2_2,
    st2_3,
    st2_4,
    st2_5,
    st2_6,
    st2_7,
]

f3_0 = pygame.Rect(52 * bw, -51 * bh, 8 * bw, 3 * bh)
f3_1 = pygame.Rect(60 * bw, -52 * bh, 8 * bw, bh)
f3_2 = pygame.Rect(68 * bw, -54 * bh, 2 * bw, 2 * bh)
f3_3 = pygame.Rect(70 * bw, -56 * bh, 2 * bw, 2 * bh)
f3_4 = pygame.Rect(65 * bw, -57 * bh, 2 * bw, bh)
f3_5 = pygame.Rect(72 * bw, -58 * bh, 2 * bw, 10 * bh)
f3_6 = pygame.Rect(76 * bw, -55 * bh, 2 * bw, 7 * bh)
f3_7 = pygame.Rect(78 * bw, -53 * bh, 2 * bw, bh)
f3_8 = pygame.Rect(80 * bw, -52 * bh, 11 * bw, bh)
f3_9 = pygame.Rect(91 * bw, -54 * bh, bw, 2 * bh)
f3_10 = pygame.Rect(86 * bw, -55 * bh, 3 * bw, bh)
f3_11 = pygame.Rect(85 * bw, -60 * bh, bw, bh)
f3_12 = pygame.Rect(86 * bw, -60 * bh, bw, 2 * bh)
f3_13 = pygame.Rect(89 * bw, -60 * bh, 5 * bw, 2 * bh)

w3_0 = pygame.Rect(84 * bw, -60 * bh, bw, 6 * bh)
w3_1 = pygame.Rect(92 * bw, -58 * bh, bw, 4 * bh)
w3_2 = pygame.Rect(92 * bw, -64 * bh, bw, 2 * bh)

st3_0 = pygame.Rect(85 * bw, -60 * bh - 1, bw, 6 * bh)

og_floor_col_3 = [
    f3_0,
    f3_1,
    f3_2,
    f3_3,
    f3_4,
    f3_5,
    f3_6,
    f3_7,
    f3_8,
    f3_9,
    f3_10,
    f3_11,
    f3_12,
    f3_13,
    w3_0,
    w3_1,
    w3_2,
]

og_stair_col_3 = [
    st3_0,
]


f4_0 = f3_13
f4_1 = pygame.Rect(82 * bw, -68 * bh, 12 * bw, bh)
f4_2 = pygame.Rect(86 * bw, -70 * bh, 2 * bw, 2 * bh)

w4_0 = pygame.Rect(92 * bw, -64 * bh, bw, 2 * bh)
w4_1 = pygame.Rect(94 * bw, -80 * bh, bw, 20 * bh)

st4_0 = pygame.Rect(93 * bw, -68 * bh - 1, bw, 8 * bh)

og_floor_col_4 = [
    f4_0,
    f4_1,
    f4_2,
    w4_0,
    w4_1,
]

og_stair_col_4 = [
    st4_0,
]
collisions = {
    "Cutman_Stage_Segment_1": [og_floor_col, og_stair_col],
    "Cutman_Stage_Segment_2": [og_floor_col_2, og_stair_col_2],
    "Cutman_Stage_Segment_3": [og_floor_col_3, og_stair_col_3],
    "Cutman_Stage_Segment_4": [og_floor_col_4, og_stair_col_4],
}
