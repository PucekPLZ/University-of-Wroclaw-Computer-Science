from turtle import *
import random
import sys
from duze_cyfry import daj_cyfre
import numpy as np

#CONFIG
#------------------
#N = 2
sys.setrecursionlimit(1500)
hideturtle()
tracer(0, 1)
pensize(1)
speed("fastest")

def move(x, y):
    pu()
    goto(x, y)
    pd()

def ri(x, y):
    return random.randint(x, y)
#------------------
N = 80
bok = 10
sx = -400
sy = -350
#Tpos = N * [ N * [0]]
#Tpos = np.empty((N, 0)).tolist()
used = {tuple([-1, -1])}

def kwadrat(bok, kolor):
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill() 

def rysuj(n, x, y, bok, kolor):
    xa = ((x*bok)+1) + sx
    ya = ((y*bok)+1) + sy
    T = daj_cyfre(n)
    for j in range(5):
            for k in range(5):
                move(xa, ya)
                if T[j][k] == "#":
                    kwadrat(bok, kolor)
                xa += bok
            xa -= bok * 5
            ya -= bok

def sprawdz(x, y, n):
    T = daj_cyfre(n)
    for j in range(5):
            for k in range(5):
                if T[j][k] == "#":
                    if used & {tuple([x, y])}:
                        return False
                x += 1
            x -= 5
            y -= 1
    return True

def wpisz(x, y, n):
    T = daj_cyfre(n)
    for j in range(5):
            for k in range(5):
                if T[j][k] == "#":
                    used.add(tuple([x, y]))
                x += 1
            x -= 5
            y -= 1

def mozaika(T, N, bok, r):
    while r > 0:
        rx = random.randint(0, N-5)
        ry = random.randint(0, N-5)
        n = random.randint(0, 9)
        if(sprawdz(rx, ry, n)):
            wpisz(rx, ry, n)
            kolor = random.choice(T)
            #kolor = np.array([random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1)])
            rysuj(n, rx, ry, bok, kolor)
            r -= 1
kolor1 = np.array([1,1,0.5])
kolor2 = np.array([1,0.5,0.8])
kolor3 = np.array([0.5,0.3,0.8])
kolor4 = np.array([0.8,0.2,0.2])
kolor5 = np.array([0.2,0.5,1])

KOLORY = [kolor1, kolor2, kolor3, kolor4, kolor5]
#KOLORY = ["black", "green", "gray", "lime"]
mozaika(KOLORY, N, bok, 50)

input('Koniec rysowania')