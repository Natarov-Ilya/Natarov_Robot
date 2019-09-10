#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down(2)
    f()
    while not wall_is_on_the_right():
        move_right(2)
        f()
    move_left(2)
    move_up()

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
