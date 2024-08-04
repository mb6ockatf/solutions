#!/usr/bin/env python3
from turtle import speed, up, forward, right, goto, dot, left, reset, color


def set_default():
    speed(0)
    left(90)
    color("blue")
    return 30


k = set_default()


def task_47210():
    for i in range(7):
        forward(10 * k)
        right(120)
    up()
    for x in range(0, 10):
        for y in range(0, 10):
            goto(x * k, y * k)
            dot(4)
    input()
    reset()


def task_47303():
    k = set_default()
    for _ in range(4):
        forward(5 * k)
        right(90)
        forward(10 * k)
        right(90)
    up()
    for x in range(0, 12):
        for y in range(0, 8):
            goto(x * k, y * k)
            dot(6)
    input()
    reset()


def task_47307():
    k = set_default()
    for _ in range(4):
        forward(10 * k)
        right(60)
        forward(10 * k)
        right(120)
    up()
    for x in range(0, 10):
        for y in range(0, 15):
            goto(x * k, y * k)
            dot(6, "orange")
    input()
    reset()


def task_47390():
    k = set_default()
    for _ in range(12):
        right(60)
        forward(1 * k)
        right(60)
        forward(1 * k)
        right(270)
    up()
    for x in range(-3, 6):
        for y in range(-7, 2):
            goto(x * k, y * k)
            dot(6, "orange")
    input()
    reset()


def task_47404():
    k = set_default()
    for _ in range(4):
        forward(10 * k)
        right(90)
    right(30)
    color("purple")
    for _ in range(5):
        forward(6 * k)
        right(60)
        forward(6 * k)
        right(120)
    up()
    for x in range(-2, 12):
        for y in range(-1, 11):
            goto(x * k, y * k)
            dot(6, "pink")
    input()
    reset()


def task_58245():
    k = set_default()
    right(60)
    for _ in range(2):
        forward(10 * k)
        right(120)
        forward(5 * k)
        right(240)
    right(120)
    forward(3 * k)
    right(90)
    forward(k * 20 * sqrt(3))
    right(90)
    forward(8 * k)
    right(120)
    for _ in range(2):
        forward(10 * k)
        left(120)
        forward(5 * k)
        left(240)
    up()
    for x in range(-18, 20):
        for y in range(-4, 8):
            goto(x * k, y * k)
            dot(6, "orange")
    input()
    reset()


def task_59684():
    k = set_default()
    for _ in range(2):
        forward(10 * k)
        right(90)
        forward(18 * k)
        right(90)
    up()
    forward(5 * k)
    right(90)
    forward(7 * k)
    left(90)
    down()
    for _ in range(2):
        forward(10 * k)
        right(90)
        forward(7 * k)
        right(90)
    up()
    for x in range(0, 20):
        for y in range(0, 16):
            goto(x * k, y * k)
            dot(6, "orange")
    input()
    reset()


if __name__ == "__main__":
    task_59684()
