#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    a=1
    while not wall_is_beneath():
        move_down()
        a=a+1
    i = a
    while i > 1:
        for x in range(1, i - 1, 1):
            move_right()
            fill_cell()
        for x in range(1, i - 2, 1):
            move_left()
        move_up()
        i = i - 2
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_right():
        move_right()
    i = a
    while i > 1:
        for x in range (1, i - 1, 1):
            move_up()
            fill_cell()
        for x in range (1, i - 2, 1):
            move_down()
        move_left()
        i = i - 2
    while not wall_is_on_the_right():
        move_right()
    while not wall_is_above():
        move_up()
    i = a
    while i > 1:
        for x in range(1, i - 1, 1):
            move_left()
            fill_cell()
        for x in range(1, i - 2, 1):
            move_right()
        move_down()
        i = i - 2
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()
    i = a
    while i > 1:
        for x in range(1, i - 1, 1):
            move_down()
            fill_cell()
        for x in range(1, i - 2, 1):
            move_up()
        move_right()
        i = i - 2
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()




if __name__ == '__main__':
    run_tasks()
