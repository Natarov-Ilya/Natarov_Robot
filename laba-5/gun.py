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
screen1 = canv.create_text(400, 300, text='', font='28')
gun1 = m.Gun(canv)

def new_game(event=''):
	global gun, target1, screen1, balls, bullet
	target1.new_target()
	bullet = 0
	canv.bind('<Button-1>', gun1.fire_start)
	canv.bind('<ButtonRelease-1>', gun1.fire_end)
	canv.bind('<Motion>', gun1.targetting)
	balls = []
	target1.live = 1
	while target1.live or balls:
		for ball in m.balls:
			ball.move()
			if time.time() - ball.birthtime > 5:
				canv.delete(ball.id)
				m.balls.remove(ball)
			if ball.hittest(target1) and target1.live:
				target1.live = 0
				target1.hit()
				canv.bind('<Button-1>', '')
				canv.bind('<ButtonRelease-1>', '')
				canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
		canv.update()
		time.sleep(0.03)
		gun1.targetting()
		gun1.power_up()
		
	canv.itemconfig(screen1, text='')
	canv.delete(gun1)
	root.after(750, new_game)


new_game()

tk.mainloop()
