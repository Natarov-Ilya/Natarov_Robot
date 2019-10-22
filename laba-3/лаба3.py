from graph import *
from math import fabs
from math import sin
from math import cos
from math import pi
from time import sleep

car_obj = list()
rot_car_obj = list()
step = False


def draw_built(x, y, x1, y1, color):
    penColor(color)
    brushColor(color)
    rectangle(x, y, x1, y1)


def draw_car(x, y, color):
    brushColor(color)
    penColor(color)
    car_obj.append(rectangle(x, y, x + 250, y + 30))
    car_obj.append(rectangle(x + 100, y, x + 220, y - 25))
    brushColor("white")
    penColor("white")
    car_obj.append(rectangle(x + 120, y - 5, x + 150, y - 20))
    car_obj.append(rectangle(x + 170, y - 5, x + 200, y - 20))
    brushColor("green")
    penColor("green")
    car_obj.append(circle(x + 60, y + 30, 15))
    car_obj.append(circle(x + 200, y + 30, 15))


def draw_small_car(x, y, k, color):
    brushColor(color)
    penColor(color)
    car_obj.append(rectangle(x, y, x + 250 / k, y + 30 / k))
    car_obj.append(rectangle(x + 100 / k, y, x + 220 / k, y - 25 / k))
    brushColor("white")
    penColor("white")
    car_obj.append(rectangle(x + 120 / k, y - 5 / k, x + 150 / k, y - 20 / k))
    car_obj.append(rectangle(x + 170 / k, y - 5 / k, x + 200 / k, y - 20 / k))
    brushColor("green")
    penColor("green")
    car_obj.append(circle(x + 60 / k, y + 30 / k, 15 / k))
    car_obj.append(circle(x + 200 / k, y + 30 / k, 15 / k))


def fence():
    brushColor("white")
    penColor("white")
    length = 5
    x = 0
    for i in range(34):
        polygon([(x, 400), (x + length, 400), (x + 3 * length, 350), (x + 2 * length, 350), (x, 400)])
        x = x + length * 3


def draw_all_car(x, y):
    draw_car(x - 21, y - 15, "orange")
    draw_car(x - 14, y - 10, (229, 240, 26))
    draw_car(x - 7, y - 5, "orange")
    draw_car(x, y, "yellow")
    penColor("yellow")
    brushColor("white")
    car_obj.append(polygon([
        (x - 21 + 100, y - 15),
        (x - 21 + 100, y - 15 - 25),
        (x + 100, y - 25),
        (x + 100, y),
        (x - 21 + 100, y - 15)
    ]))


def draw_all_cars_trans(x, y, k):
    draw_small_car(x - 21 / k, y - 15 / k, k, "orange")
    draw_small_car(x - 14 / k, y - 10 / k, k, (229, 240, 26))
    draw_small_car(x - 7 / k, y - 5 / k, k, "orange")
    draw_small_car(x, y, k, "yellow")
    penColor("yellow")
    brushColor("white")
    car_obj.append(polygon([
        (x - 21 / k + 100 / k, y - 15 / k),
        (x - 21 / k + 100 / k, y - 15 / k - 25 / k),
        (x + 100 / k, y - 25 / k), (x + 100 / k, y),
        (x - 21 / k + 100 / k, y - 15 / k)
    ]))


def draw_ellips(a, b, x, y, color):
    points = list()
    moveTo(x - a / 2)
    for i in range((x - a) * 10, (x + a) * 10, 1):
        xi = i / 10
        yi = y + (b ** 2 * (1 - (i / 10 - x) ** 2 / a ** 2)) ** 0.5
        points.append((xi, yi))
    brushColor(color)
    penColor(color)
    polygon(points)


def draw_all_ellips():
    draw_built(0, 400, 500, 600, (229, 240, 110))
    draw_ellips(500, 200, 50, 407, (44, 232, 60))
    draw_ellips(500, 100, 50, 407, (11, 161, 41))
    draw_ellips(500, 50, 50, 407, (229, 240, 110))


def draw_all_builts():
    draw_built(100, 0, 160, 350, "yellow")
    draw_built(190, 0, 220, 350, "yellow")
    draw_built(250, 0, 300, 350, "yellow")
    draw_built(350, 0, 440, 350, "yellow")
    draw_built(0, 0, 60, 350, "yellow")
    for i in range(71):
        draw_built(0, 5 * i, 600, 5 * i + 2, "white")
    draw_built(20, 140, 230, 400, (255, 255, 0))
    for i in range(22):
        draw_built(20 + i * 10, 140, 20 + i * 10 + 6, 400, "white")
    draw_built(0, 350, 500, 400, (255, 255, 0))
    draw_built(0, 400, 600, 410, "orange")
    draw_built(0, 340, 600, 350, "orange")
    fence()


def move_car(dx, dy):
    for i in car_obj:
        moveObjectBy(i, dx, dy)


def ellipse(xo, yo, a, b, color, angle):
    points = list()
    for i in range(-a * 10, a * 10, 1):
        xold = i / 10
        yold = (b ** 2 * (1 - (i / 10) ** 2 / a ** 2)) ** 0.5
        xnew = xo + xold * cos(angle) + yold * sin(angle)
        ynew = yo + yold * cos(angle) - xold * sin(angle)
        points.append((xnew, ynew))
    for i in range(a * 10, -a * 10, -1):
        xold = i / 10
        yold = -((b ** 2 * (1 - (i / 10) ** 2 / a ** 2)) ** 0.5)
        xnew = xo + xold * cos(angle) + yold * sin(angle)
        ynew = yo + yold * cos(angle) - xold * sin(angle)
        points.append((xnew, ynew))
    brushColor(color)
    return polygon(points)


def mine(x, y):
    brushColor("black")
    ellipse(x, y, 20, 2, "black", 0)
    ellipse(x, y, 20, 2, "black", pi / 6)
    ellipse(x, y, 20, 2, "black", pi / 3)
    ellipse(x, y, 20, 2, "black", pi / 2)
    ellipse(x, y, 20, 2, "black", 2 * pi / 3)
    ellipse(x, y, 20, 2, "black", 5 * pi / 6)
    ellipse(x, y, 10, 10, "black", 0)


def fire(x, y):
    brushColor("red")
    polygon([(x, y), (x - 40, y - 10), (x - 20, y - 10), (x - 30, y - 20), (x - 10, y - 20), (x - 20, y - 30),
             (x - 10, y - 30), (x, y - 40)])
    polygon([(x, y), (x + 40, y - 10), (x + 20, y - 10), (x + 30, y - 20), (x + 10, y - 20), (x + 20, y - 30),
             (x + 10, y - 30), (x, y - 40)])


def grey_crane():
    draw_built(290, 80, 310, 340, "grey")
    ellipse(300, 65, 40, 40, "grey", 0)


def turn(xo, yo, xold, yold, angle):
    x = xo + xold * cos(angle) + yold * sin(angle)
    y = yo + yold * cos(angle) - xold * sin(angle)
    return x, y


def crane(xo, yo, a, b, color, angle):
    global obj_crane
    x1old = a
    y1old = -b
    x1, y1 = turn(xo, yo, x1old, y1old, angle)
    x2old = a
    y2old = b
    x2, y2 = turn(xo, yo, x2old, y2old, angle)
    x3old = -a
    y3old = -b
    x3, y3 = turn(xo, yo, x3old, y3old, angle)
    x4old = -a
    y4old = b
    x4, y4 = turn(xo, yo, x4old, y4old, angle)

    penColor(color)
    brushColor(color)
    obj_crane = polygon([(x1, y1), (x2, y2), (x4, y4), (x3, y3)])


def update():
    global a, obj_crane, step
    if not step:
        deleteObject(obj_crane)
        a = a + pi / 180
        crane(300, 65, 300, 10, "grey", a)
    if xCoord(car_obj[0]) <= -200:
        move_car(800, -50)
    if xCoord(car_obj[0]) <= 150 and yCoord(car_obj[0]) >= 520:
        fire(100, 570)
        step = True
        return
    move_car(-5, 0.5)


draw_all_ellips()
draw_all_builts()
draw_all_cars_trans(600, 450, 1.6)
grey_crane()
mine(100, 570)
a = 0
obj_crane = 0
crane(300, 65, 300, 10, "grey", a)
onTimer(update, 30)
run()
