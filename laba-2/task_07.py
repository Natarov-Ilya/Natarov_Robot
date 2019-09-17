# рисует спираль
import turtle as t
import time

t.shape ("turtle")
a=5
for x in range(1, 360, 1):
	t.forward(0.01*a)
	t.left(5)
	a=a+5
time.sleep(3)