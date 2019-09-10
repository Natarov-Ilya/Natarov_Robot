#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    i=1
    while not wall_is_on_the_right():
        fill_cell()
        for x in range (1,i+1,1):
            if not wall_is_on_the_right():
                move_right()
        i=i+1


if __name__ == '__main__':
    run_tasks()
