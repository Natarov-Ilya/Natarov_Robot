#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    while not wall_is_on_the_right():
        while not wall_is_beneath():
            fill_cell()
            move_down()
        move_up()
        while cell_is_filled():
            move_up()
        move_right()
        move_down(2)
    while not wall_is_on_the_left():
        move_left()
    move_right()


if __name__ == '__main__':
    run_tasks()
