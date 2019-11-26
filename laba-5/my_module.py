from random import randrange as rnd, choice
import tkinter as tk
import math
import time
bullet = 0
balls = []
class Ball():
	""" Снаряд в виде круга
	Параметры:
		x, y - координаты
		r - радиус
		vx, vy - компоненеты скорости
		color - цвет заливки
		id - визуализация снаряда (oval)
	Методы:
		__init__ - задает начальные значения параметров
		set_coords - меняет координаты по которым рисуется снаряд
		move - двигает снаряд
		hittest - контролирует сталкновение с целями 
	"""
	def __init__(self, canv, x=40, y=450):
		""" Конструктор класса ball

		Args:
		x - начальное положение мяча по горизонтали
		y - начальное положение мяча по вертикали
		"""
		self.canv = canv
		self.x = x
		self.y = y
		self.r = 10
		self.vx = 0
		self.vy = 0
		self.birthtime = time.time()
		self.color = choice(['blue', 'green', 'red', 'brown'])
		self.id = self.canv.create_oval(
				self.x - self.r,
				self.y - self.r,
				self.x + self.r,
				self.y + self.r,
				fill=self.color
		)
		self.live = 5

	def set_coords(self):
		self.canv.coords(
				self.id,
				self.x - self.r,
				self.y - self.r,
				self.x + self.r,
				self.y + self.r
		)

	def move(self):
		"""Переместить мяч по прошествии единицы времени.

		Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
		self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
		и стен по краям окна (размер окна 800х600).
		"""
		if (self.x < 0):
			self.vx = -self.vx
		if (self.x > 800):
			self.vx = -self.vx
		if (self.y < 0):
			self.vy = -self.vy
		if (self.y > 600 - self.r):
			self.vx = 0
			self.vy = 0
			self.y = 600 - self.r
		if (self.y < 600 - self.r):
			self.vy -= 2
		self.x += self.vx
		self.y -= self.vy
		self.set_coords()

	def hittest(self, obj):
		"""Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

		Args:
			obj: Обьект, с которым проверяется столкновение.
		Returns:
			Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
		"""
		if (((obj.x - self.x)**2 + (obj.y - self.y)**2)**0.5 <= obj.r + self.r): 
			return True
		else:
			return False

class Gun():
	""" Пушка
	Параметры:
		power - сила выстрила (модуль скорости снаряда)
		flag - флаг, показывающий нажата или нет кнопка мыши
		angle - угол межды осью х и вектором скорости
		id - визуализация пушки
	Методы:
		__init__ - задает начальные значения параметров
		fire_start - вызывается, когда нажимают кнопку мыши, начинает прицеливание и установку силы выстрела
		fire_end - вызывается, когда отпускают кнопки мыши, производит выстрел
		targetting - управляет прицеливанием
		power_up - управляет силой выстрела
	"""
	def __init__(self, canv):
		self.canv = canv
		self.power = 10
		self.flag = 0
		self.angle = 1
		self.id = self.canv.create_line(20, 450, 50, 420, width=7)

	def fire_start(self, event):
		self.flag = 1

	def fire_end(self, event):
		"""Выстрел мячом.

		Происходит при отпускании кнопки мыши.
		Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
		"""
		global balls, bullet
		bullet += 1
		new_ball = Ball(self.canv)
		new_ball.r += 5
		self.angle = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
		new_ball.vx = self.power * math.cos(self.angle)
		new_ball.vy = - self.power * math.sin(self.angle)
		balls += [new_ball]
		self.flag = 0
		self.power = 10

	def targetting(self, event=0):
		"""Прицеливание. Зависит от положения мыши."""
		if event:
			self.angle = math.atan((event.y-450) / (event.x-20))
		if self.flag:
			self.canv.itemconfig(self.id, fill='orange')
		else:
			self.canv.itemconfig(self.id, fill='black')
		self.canv.coords(self.id, 20, 450,
					20 + max(self.power, 20) * math.cos(self.angle),
					450 + max(self.power, 20) * math.sin(self.angle)
					)

	def power_up(self):
		if self.flag:
			if self.power < 100:
				self.power += 1
			self.canv.itemconfig(self.id, fill='orange')
		else:
			self.canv.itemconfig(self.id, fill='black')


class Target():
	""" Мишень
	Параметры:
		points - количество попаданий
		live - количество жизней мишени
		id - визуализация мишени (oval)
		id_points - визуализация счетчика попаданий
	Методы:
		__init__ - задает начальные значения параметров
		new_target - создает новую мишень
		hit - отслеживает попадания снаряда в мишень
	"""
	def __init__(self, canv):
		self.canv = canv
		self.points = 0
		self.live = 1
		self.id = self.canv.create_oval(0,0,0,0)
		self.id_points = self.canv.create_text(30,30,text = self.points,font = '28')
		self.new_target()

	def new_target(self):
		""" Инициализация новой цели. """
		x = self.x = rnd(600, 780)
		y = self.y = rnd(300, 550)
		r = self.r = rnd(2, 50)
		color = self.color = 'red'
		self.canv.coords(self.id, x-r, y-r, x+r, y+r)
		self.canv.itemconfig(self.id, fill=color)

	def hit(self, points=1):
		"""Попадание шарика в цель."""
		self.canv.coords(self.id, -10, -10, -10, -10)
		self.points += points
		self.canv.itemconfig(self.id_points, text=self.points)