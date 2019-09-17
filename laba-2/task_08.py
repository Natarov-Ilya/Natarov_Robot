# рисует квадратную спираль
import turtle as t
import time

t.shape ("turtle")
a=5
for x in range(1, 32, 1):
	t.forward(a)
	t.left(90)
	a=a+5
time.sleep(3)