from turtle import *

speed('fastest')
pensize(2)


def kwadrat(bok):
    for i in range(4):
        fd(bok)
        rt(90)


def rozeta3(a, b, n):
    for i in range(n):
        fd(a)
        kwadrat(b)
        bk(a)
        rt(360/n)

rozeta3(100, 40, 18)
rozeta3(63,35,18)
rozeta3(35,25,18)
rozeta3(20,10,12)

