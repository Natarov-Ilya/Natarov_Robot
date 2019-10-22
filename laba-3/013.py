from graph import *
from math import fabs
from math import cos
from math import sin
from math import pi
from time import sleep
import time


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


def half_ellipse(xo, yo, a, b, color, angle):
    points = list()
    for i in range(-a * 10, a * 10, 1):
        xold = i / 10
        yold = (b ** 2 * (1 - (i / 10) ** 2 / a ** 2)) ** 0.5
        xnew = xo + xold * cos(angle) + yold * sin(angle)
        ynew = yo + yold * cos(angle) - xold * sin(angle)
        points.append((xnew, ynew))
    brushColor(color)
    polygon(points)


def planet():
    ellipse(350, 150, 100, 100, "white", -(pi / 8))
    ellipse(350, 150, 80, 100, "black", -(pi / 8))
    ellipse(350, 150, 300, 30, "gray", -(pi / 8))
    ellipse(350, 150, 200, 27, "black", -(pi / 8))
    ellipse(350, 150, 190, 24, "white", -(pi / 8))
    ellipse(350, 150, 150, 21, "black", -(pi / 8))
    half_ellipse(350, 150, 100, 100, "white", pi - (pi / 8))
    half_ellipse(350, 150, 80, 100, "black", pi - (pi / 8))


def astronaut(x, y, color):
    penColor(color)
    obj.append(ellipse(x, y, 12, 12, color, 0))
    obj.append(ellipse(x + 1, y - 1, 10, 9, "black", 0))

    obj.append(ellipse(x, y + 33, 12, 22, color, 0))

    obj.append(ellipse(x + 17, y + 53, 14, 8, color, -(pi / 6)))
    obj.append(ellipse(x + 29, y + 66, 10, 8, color, -(pi / 2)))
    obj.append(ellipse(x + 37, y + 78, 10, 6, color, 0))

    obj.append(ellipse(x - 12, y + 60, 14, 8, color, (pi / 3)))
    obj.append(ellipse(x - 10, y + 76, 10, 8, color, -(pi / 3)))
    obj.append(ellipse(x - 10, y + 90, 10, 6, color, (pi / 6)))

    obj.append(ellipse(x + 16, y + 16, 7, 7, color, 0))
    obj.append(ellipse(x + 26, y + 10, 5, 5, color, 0))
    obj.append(ellipse(x + 32, y + 4, 5, 5, color, 0))

    obj.append(ellipse(x - 16, y + 16, 7, 7, color, 0))
    obj.append(ellipse(x - 26, y + 22, 5, 5, color, 0))
    obj.append(ellipse(x - 32, y + 28, 5, 5, color, 0))


def bookcase():
    brushColor(139, 69, 19)
    penColor(139, 69, 19)
    rectangle(200, 440, 500, 600)
    brushColor(102, 51, 0)
    penColor(102, 51, 0)
    rectangle(200, 440, 500, 450)
    rectangle(200, 490, 500, 500)
    rectangle(200, 540, 500, 550)
    rectangle(200, 590, 500, 600)


def book(xo, yo, x, y, color):
    brushColor(color)
    penColor(color)
    rectangle(xo, yo, x, y)


def USA(x, y):
    penSize(0.001)
    brushColor("red")
    penColor("red")
    rectangle(x, y, x + 80, y + 52)
    penColor("white")
    brushColor("white")
    for i in range(1, 12, 2):
        rectangle(x, y + 4 * i, x + 80, y + 4 * i + 3)
    penColor("blue")
    brushColor("blue")
    rectangle(x, y, x + 35, y + 28)
    for j in range(0, 3, 1):
        for i in range(0, 3, 1):
            star(x + i * 10 + 6, y + j * 10 + 6, 3, "white")
    penColor("white")
    line(x, y, x, y + 150)


def star(x, y, r, color):
    penColor(color)
    moveTo(x, y - r)
    lineTo(x + r * sin(pi / 5), y + r * cos(pi / 5))
    lineTo(x - r * sin(2 * pi / 5), y - r * cos(2 * pi / 5))
    lineTo(x + r * sin(2 * pi / 5), y - r * cos(2 * pi / 5))
    lineTo(x - r * sin(pi / 5), y + r * cos(pi / 5))
    lineTo(x, y - r)


def up():
    global obj
    if yCoord(obj[0]) <= 100:
        USA(320, 50)
        return False
    for i in obj:
        moveObjectBy(i, 5, -5)


state = 0
obj = list()
brushColor("Black")
rectangle(0, 0, 500, 600)
planet()
bookcase()
book(200, 450, 210, 490, "red")
book(210, 460, 220, 490, "green")
book(220, 470, 230, 490, "blue")
book(250, 490, 270, 450, "yellow")
astronaut(50, 350, "gray")
onTimer(up, 50)
run()
time.sleep(3)
