from pico2d import * # pico2d.open_canvas() 앞에 안붙여도 됨 all 임포트

import math
x = 400
y = 90
speed = 10

def boy_draw(x, y):
    clear_canvas()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def move_rectangle():
    global x, y
    # 아래 -> 오른쪽
    while x < 750:
        x += speed
        boy_draw(x, y)
    # 오른쪽 -> 위
    while y < 510:
        y += speed
        boy_draw(x, y)
    # 위 -> 왼쪽
    while x > 50:
        x -= speed
        boy_draw(x, y)
    # 왼쪽 -> 아래 (시작점으로)
    while y > 90:
        y -= speed
        boy_draw(x, y)
    # 마지막에 (400, 510)까지 이동
    while x != 400 or y != 510:
        if x < 400:
            x += speed
            if x > 400: x = 400
        elif x > 400:
            x -= speed
            if x < 400: x = 400
        if y < 510:
            y += speed
            if y > 510: y = 510
        elif y > 510:
            y -= speed
            if y < 510: y = 510
        boy_draw(x, y)

def move_circle():
    global x, y
    for d in range(0, 361, 5):
        rad = math.radians(d)
        x = 400 + 210 * math.sin(rad)
        y = 300 + 210 * math.cos(rad)
        boy_draw(x, y)
    # 마지막에 (400, 510)까지 이동
    while x != 400 or y != 510:
        if x < 400:
            x += speed
            if x > 400: x = 400
        elif x > 400:
            x -= speed
            if x < 400: x = 400
        if y < 510:
            y += speed
            if y > 510: y = 510
        elif y > 510:
            y -= speed
            if y < 510: y = 510
        boy_draw(x, y)

def move_triangle():
    global x, y
    # 꼭짓점1 (400,510) -> 꼭짓점2 (190,180)
    while x > 190 or y > 180:
        if x > 190:
            x -= speed
        if y > 180:
            y -= speed
        boy_draw(x, y)
    # 꼭짓점2 (190,180) -> 꼭짓점3 (610,180)
    while x < 610:
        x += speed
        boy_draw(x, y)
    # 꼭짓점3 (610,180) -> 꼭짓점1 (400,510)
    while x > 400 or y < 510:
        if x > 400:
            x -= speed
        if y < 510:
            y += speed
        boy_draw(x, y)
    # 마지막에 (400, 510)까지 이동 (혹시 오차가 있을 경우 보정)
    while x != 400 or y != 510:
        if x < 400:
            x += speed
            if x > 400: x = 400
        elif x > 400:
            x -= speed
            if x < 400: x = 400
        if y < 510:
            y += speed
            if y > 510: y = 510
        elif y > 510:
            y -= speed
            if y < 510: y = 510
        boy_draw(x, y)

open_canvas()
hide_lattice()

grass = load_image('grass.png')
character = load_image('character.png')

while 1:
    move_rectangle()
    move_circle()
    move_triangle()

close_canvas()
