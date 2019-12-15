from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import my_module as m
# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
target1 = m.Target(canv)
target2 = m.Target(canv)
screen1 = canv.create_text(400, 300, text='', font='28')
gun1 = m.Gun(canv)
points = 0
screen_points = canv.create_text(30,30,text = points,font = '28')

def new_game(event=''):
	global gun, target1, target2, screen1, balls, bullet, points, screen_points
	if target1.live:
		target2.new_target()
		target2.live = 1
	else:
		target1.new_target()
		target1.live = 1
	canv.bind('<Button-1>', gun1.fire_start)
	canv.bind('<ButtonRelease-1>', gun1.fire_end)
	canv.bind('<Motion>', gun1.targetting)
	balls = []
	while (target1.live and target2.live) or balls:
		target1.move()
		target2.move()
		for ball in m.balls:
			ball.move()
			if time.time() - ball.birthtime > 5:
				canv.delete(ball.id)
				m.balls.remove(ball)
			if (ball.hittest(target1) and target1.live) or  (ball.hittest(target2) and target2.live):
				if ball.hittest(target1) and target1.live:
					target1.live = 0
					target1.hit()
				else:
					target2.live = 0
					target2.hit()
				canv.delete(ball.id)
				m.balls.remove(ball)
				points = points + 1
				canv.itemconfig(screen_points, text = str(points))
				canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(m.bullet) + ' выстрелов')
				canv.update()
				time.sleep(1)
				m.bullet = 0
				canv.bind('<Button-1>', '')
				canv.bind('<ButtonRelease-1>', '')
		canv.update()
		time.sleep(0.03)
		gun1.targetting()
		gun1.power_up()
	canv.itemconfig(screen1, text='')
	canv.delete(gun1)
	root.after(750, new_game)

def Start_new_game(event):
	global points
	points = 0
	m.bullet = 0
	canv.itemconfig(screen_points, text = str(points))
	target1.new_target()
	target2.new_target()
	for ball in m.balls:
		canv.delete(ball.id)

b = tk.Button(root, text="Начать новую игру")
b.bind('<Button-1>', Start_new_game)
b.pack()
new_game()
tk.mainloop()

