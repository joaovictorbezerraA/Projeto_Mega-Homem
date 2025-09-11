import pygame

bw = 3 * 16
bh = 3 * 16
of = 5
th = 3  # wall__collision_thickness


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
]
