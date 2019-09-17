# рисует многоугольники
import turtle as t
import time
import math
def polygon(n, r):
	t.pendown()
	a = r*2*math.sin(((360/(2*n))/360)*2*math.pi)
	for i in range (1, n+1, 1):
		t.forward (a)
		t.left (360/n)
	t.penup()

t.shape ("turtle")
t.penup()
r=50
for i in range (3, 9, 1):
	t.left (180 - 180*(i-2)/(2*i))
	polygon(i, r)
	t.right (180 - 180*(i-2)/(2*i))
	t.forward (30)
	r=r+30
time.sleep (10)
