#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    while not wall_is_beneath():
        move_down()
    move_right()
    move_up(2)
    while not wall_is_above():
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        while not wall_is_on_the_left():
            move_left()
        move_up()
        move_right()
    while not wall_is_beneath():
        move_down()
    move_up()



if __name__ == '__main__':
    run_tasks()
