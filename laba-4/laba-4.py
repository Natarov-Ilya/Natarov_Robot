from tkinter import *
from random import randrange as rnd, choice
import random
import math
import time
root = Tk()
root.geometry('800x600')
canvas = Canvas(root,bg='white')
canvas.pack(fill=BOTH,expand=1)
goals = 0
lap = 0
flag = 0
k = 0
j = 0
open_time = 0
colors = ['red','orange','yellow','green','blue']
resuts = []
balls = []
cube = []
def new_ball():
	global balls, k, lap, goals, flag, cube, w, exist, open_time
	colors = [0,1,2,3,4]
	balls.clear()
	k = 0
	w = rnd(1,3)
	if (w == 2):
		exist = 1
		x = rnd(100, 700)
		y = rnd(100, 700)
		a = rnd (60, 80)
		b = rnd (60, 80)
		angle = math.pi * random.random() * 2
		vx = 6 * math.cos(angle)
		vy = 6 * math.sin(angle)
		color = choice(colors)
		cube = [x, y, a, b, vx, vy, color]

	else:
		for i in range (2): 
			x = rnd(100, 700)
			y = rnd(100, 500)
			r = rnd(30, 40)
			angle = math.pi * random.random() * 2
			vx = 6 * math.cos(angle)
			vy = 6 * math.sin(angle)
			color = choice(colors)
			balls.append([x, y, r, vx, vy, color])
			k = k + 1
	if (lap < 10):
		root.after (2000, new_ball)
	else:
		flag = 1
		canvas.delete(ALL)
		canvas.create_text(400, 300, text=str(goals)+"/20", anchor=S, fill="grey", font="Verdana 24")
		if (goals>=15): 
			canvas.create_text(400, 400,  text="Excellent!", anchor=S, fill="grey", font="Verdana 24")
		else: 
			if (goals>=10):
				canvas.create_text(400, 400,  text="not bad", anchor=S, fill="grey", font="Verdana 24")
			else:
				canvas.create_text(400, 400,  text="try again...", anchor=S, fill="grey", font="Verdana 24")
		print ("Введите свою имя")
		table ()
		open_time = open_time + 1
		canvas.create_text(400, 500, text="Start new game", anchor=S, fill="blue", font="Verdana 24")
		canvas.bind('<Button-1>', getXY)
		return
	lap = lap + 1
def move_ball(n):
	global balls, k, colors
	x = balls[n][0]
	y = balls[n][1]
	r = balls[n][2]
	vx = balls[n][3]
	vy = balls[n][4]
	n_color = balls[n][5]
	color = colors [n_color]
	if (y <= r):
		y = r
		vy = - vy
	if (y >= 600 - r):
		y = 600 -r
		vy = - vy
	if (x <= r):
		x = r
		vx = - vx
	if (x >= 800 - r):
		x = 800 -r
		vx = - vx
	i = 0
	while (i < k):
		if (i != n and ((x - balls[i][0])**2 + (y - balls[i][1])**2)**0.5 <= balls[i][2] + r):
			vx = - vx
			vy = - vy
			balls[i][3] = - balls[i][3]
			balls[i][4] = - balls[i][4]
		i = i + 1
	x = x + vx
	y = y + vy
	canvas.create_oval(x - r, y - r, x + r, y + r, fill = color, width=2, tag = "1")
	balls[n] = [x, y, r, vx, vy, n_color]

def move_cube():
	global cube, colors
	x = cube[0]
	y = cube[1]
	a = cube[2]
	b = cube[3]
	vx = cube[4]
	vy = cube[5]
	n_color = cube[6]
	color = colors[n_color]
	if (y <= 0):
		y = 0
		vy = - vy
	if (y >= 600 - b):
		y = 600 - b
		vy = - vy
	if (x <= 0):
		x = 0
		vx = - vx
	if (x >= 800 - a):
		x = 800 - a
		vx = - vx
	x = x + vx
	y = y + vy
	canvas.create_rectangle(x, y, x+a, y+b, fill = color)
	cube = [x, y, a, b, vx, vy, n_color]

def update():
	global balls, k, j, flag, w, cube
	if (flag == 1):
		return
	j = 0
	canvas.delete(ALL)
	if (w == 2):
		if (exist == 1):
			move_cube()
	else:
		while (j < k):
			move_ball(j)
			j = j + 1
	root.after(10, update)
def getXY(event):
	if (event.y > 470 and event.y < 500 and event.x > 280 and event.x < 530):
		new_game()
def new_game():
	global flag, lap, goals
	flag = 0
	lap = 0
	goals = 0
	canvas.bind('<Button-1>', click)
	new_ball()
	update()

def click(event):
	global goals, j, k, w, cube, balls, exist
	i = 0
	if (w == 2):
		if (event.x > cube[0] and event.x < cube[0]+cube[2] and event.y > cube[1] and event.y < cube[1] + cube[3]):
			goals = goals + 2
			exist = 0
			canvas.delete(ALL)
	else:
		while (i < k):
			if (((event.x - balls[i][0])**2 + (event.y - balls[i][1])**2)**0.5 <= balls[i][2]):
				goals = goals + 1
				del balls[i]
				k = k - 1
				j = 0
				break
			i = i + 1
def table():
	global resuts
	name = input()
	print (name, str(goals))
	if (open_time == 0):
		resuts.append("14 Вася Пупкин")
		resuts.append("10 Маша Иванова")


	if (goals < 10):
		resuts.append("0" + str(goals) + " " + name)
	else:
		resuts.append(str(goals) + " " + name)
	resuts.sort()
	resuts.reverse()

	i = 0
	f = open("Лучшие игроки.txt", "w")
	for r in resuts:
		f.write(resuts[i] + "\n")
		i = i + 1
	f.close()



canvas.bind('<Button-1>', click)
new_ball()
update()
mainloop()