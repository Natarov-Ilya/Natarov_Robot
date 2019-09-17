import turtle as t
import time

def star(n):
	t.pendown()
	t.right(90-90/n)
	for i in range(1, n+1, 1):
		t.forward(200)
		t.right(180-180/n)
	t.left(90-90/n)
	t.penup()
t.penup()	
t.goto(-200,100)
star(5)
t.goto(200,100)
star(11)

time.sleep(3)