#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_right(2)
    move_down()
    fill_cell()
    move_down()
    fill_cell()
    move_left()
    fill_cell()
    move_right(2)
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up(2)
    move_left()


if __name__ == '__main__':
    run_tasks()
