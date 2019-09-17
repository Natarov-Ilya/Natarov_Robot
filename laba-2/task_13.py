# рисует смайл
import turtle as t
import time
import math

def arc(r):
	t.pendown()
	for i in range(1, 51, 1):
		t.forward(2*math.pi*r/50)
		t.left(360/100)
	t.pendown()
def circle(r):
	t.pendown()
	for i in range(1, 101, 1):
		t.forward(2*math.pi*r/100)
		t.left(360/100)
	t.penup()

t.shape("turtle")
t.penup()

t.goto(0,-200)
t.fillcolor("yellow")
t.begin_fill()
circle(200)
t.end_fill()

t.goto(-70,70)
t.fillcolor("blue")
t.begin_fill()
circle(30)
t.end_fill()

t.goto(70,70)
t.fillcolor("blue")
t.begin_fill()
circle(30)
t.end_fill()

t.goto(0,30)
t.color("black")
t.width(15)
t.pendown()
t.goto(0,-10)
t.penup()

t.goto(-100,-20)
t.width(15)
t.color("red")
t.left(-90)
arc(50)


time.sleep(3)