from pico2d import *
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
    while x < 750:
        x += speed
        boy_draw(x, y)
    while y < 510:
        y += speed
        boy_draw(x, y)
    while x > 50:
        x -= speed
        boy_draw(x, y)
    while y > 90:
        y -= speed
        boy_draw(x, y)
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
    while x > 190 or y > 180:
        if x > 190:
            x -= speed
        if y > 180:
            y -= speed
        boy_draw(x, y)
    while x < 610:
        x += speed
        boy_draw(x, y)
    while x > 400 or y < 510:
        if x > 400:
            x -= speed
        if y < 510:
            y += speed
        boy_draw(x, y)
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
