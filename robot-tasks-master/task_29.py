#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    i=0
    while not wall_is_on_the_right() and i<3:
        if cell_is_filled():
            i=i+1
        else:
            i=0
        move_right()
    if i==3:
        move_left()


if __name__ == '__main__':
    run_tasks()
