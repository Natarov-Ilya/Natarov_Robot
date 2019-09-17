#рисует спираль
import turtle as t
import time

def arc(dl):
	for i in range(1, 51, 1):
		t.forward(dl)
		t.right(360/100)
t.penup()
t.goto(-300,0)
t.pendown()
t.left(90)
for i in range(1, 7, 1):
	arc(2)
	arc(0.2)
t.shape ("turtle")
t.penup()
time.sleep(3)