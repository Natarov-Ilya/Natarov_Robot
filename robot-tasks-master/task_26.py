#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    move_down()
    f()
    while not wall_is_on_the_right():
        move_right(2)
        f()
    while not wall_is_on_the_left():
        move_left()
    move_down()
    while not wall_is_beneath():
        move_down(3)
        f()
        while not wall_is_on_the_right():
            move_right(2)
            f()
        while not wall_is_on_the_left():
            move_left()
        move_down()
    move_up(2)


def f():
    fill_cell()
    move_right()
    fill_cell()
    move_up()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    move_right()
    fill_cell()


if __name__ == '__main__':
    run_tasks()
