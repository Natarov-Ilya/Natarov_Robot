#рисует круг
import turtle as t
from time import sleep

t.shape('turtle')
for i in range(1, 101, 1):
	t.forward(10)
	t.left(360/100)
sleep(3)