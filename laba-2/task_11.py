# рисует бабочку из окружностей
import turtle as t
import time

def circle(dl):
	for i in range(1, 101, 1):
		t.forward(dl)
		t.left(360/100)

t.shape ("turtle")
t.left (90)
dl=2
for i in range(1, 9, 1):
	circle(dl)
	dl=dl+1
t.left (180)
dl=2
for i in range(1, 9, 1):
	circle(dl)
	dl=dl+1
time.sleep(5)