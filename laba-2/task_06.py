# рисует паучка
import turtle as t
import time

t.shape ("turtle")
for x in range(1, 13, 1):
	t.forward(50)
	t.stamp()
	t.backward(50)
	t.left(360/12)
time.sleep(3)