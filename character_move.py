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

def circle_move(x, y):
    for d in range(0, 361, 5):
        rad = math.radians(d)
        x = 400 + 210 * math.sin(rad)
        y = 300 + 210 * math.cos(rad)
        boy_draw(x, y)

def triangle_move(x, y):
    point1 = (400, 510)
    point2 = (700, 210)
    point3 = (100, 210)
    points = [point1, point2, point3, point1]

    for px, py in points:
        while x != px or y != py:
            if x < px: x += speed
            if x > px: x -= speed
            if y < py: y += speed
            if y > py: y -= speed
            boy_draw(x, y)

open_canvas()
hide_lattice()

grass = load_image('grass.png')
character = load_image('character.png')

while 1:
    while x < 750:
        x += speed
        boy_draw(x, y)
    while y < 510:
        y += speed
        boy_draw(x, y)
    while x > 50:
        x -= speed
        boy_draw(x, y)
        if x == 400 and y == 510:
            circle_move(x, y)
            triangle_move(x, y)

    while y != 90:
        y -= speed
        boy_draw(x, y)

close_canvas()


