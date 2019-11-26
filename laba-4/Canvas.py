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
k = 0
j = 0
colors = ['red','orange','yellow','green','blue']
color = choice(colors)
balls = []
def new_ball():
	global balls, k
	#colors = ['red','orange','yellow','green','blue']
	x = rnd(100, 700)
	y = rnd(100, 500)
	r = rnd(30, 40)
	angle = math.pi * random.random() * 2
	vx = 4 * math.cos(angle)
	vy = 4 * math.sin(angle)
	#color = choice(colors)
	balls.append([x, y, r, vx, vy])
	k = k + 1
def move_ball(n):
	global balls, k
	x = balls[n][0]
	y = balls[n][1]
	r = balls[n][2]
	vx = balls[n][3]
	vy = balls[n][4]
	#color = balls[n][5]
	if (y <= r):
		y = r
		vy = - vy
	if (y >= 600 - r):
		y = 600 -r
		vy = - vy
	if (x <= r):
		x = r
		vx = - vx
	if (x >= 600 - r):
		x = 600 -r
		vx = - vx
	i = 0
	while (i < k):
		if (i != n and ((x - balls[i][0])**2 + (y - balls[i][1])**2)**0.5 <= balls[i][2]):
			vx = - vx
			vy = - vy
			balls[i][3] = - balls[i][3]
			balls[i][4] = - balls[i][4]
			i = i + 1
	x = x + vx
	y = y + vy
	canvas.create_oval(x - r, y - r, x + r, y + r, fill = color, width=2, tag = "1")
	balls[n] = [x, y, r, vx, vy]

def update():
	global balls, k, j
	canvas.delete(ALL)
	if (k < 2):
		new_ball()
	j = 0
	while (j < k):
		move_ball(j)
		j = j + 1
	root.after(20, update)


def click(event):
	global goals, j, k
	i = 0
	while (i < k):
		if (((event.x - balls[i][0])**2 + (event.y - balls[i][1])**2)**0.5 <= balls[i][2]):
			goals = goals + 1
			del balls[i]
			k = k - 1
			j = 0
			#break
		i = i + 1
canvas.bind('<Button-1>', click)
update()
mainloop()
"""
def new_ball():
	global x, y, r, k, ball_1
	
	k+=1
	if k == 11:
		canvas.create_text(400, 300, text=str(goals)+"/10", anchor=S, fill="grey", font="Verdana 24")
		if (goals>=8): 
			canvas.create_text(400, 400,  text="Excellent!", anchor=S, fill="grey", font="Verdana 24")
		else: 
			if (goals>=5):
				canvas.create_text(400, 400,  text="not bad", anchor=S, fill="grey", font="Verdana 24")
			else:
				canvas.create_text(400, 400,  text="try again...", anchor=S, fill="grey", font="Verdana 24")
		return
	

	ball_1 = canvas.create_oval(x-r, y-r, x+r, y+r, fill = choice(colors), width=2, tag = 'oval_1')
	root.after(10, new_ball)
"""