import turtle as t
from time import sleep

def q(a):
	for i in range(1, 5, 1):
		t.pendown()
		t.forward(a)
		t.left(90)
		t.penup()


t.shape('turtle')
a=4
for i in range(1, 11, 1):
	q(a)
	a=a+16
	t.right(90)
	t.forward(8)
	t.right(90)
	t.forward(8)
	t.right(180)
sleep(3)