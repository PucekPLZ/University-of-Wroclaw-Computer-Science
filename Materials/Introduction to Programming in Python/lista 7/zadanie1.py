import io
from turtle import *
import random
import sys
import numpy as np

def move(x, y):
    pu()
    goto(x, y)
    pd()

def kwadrat(bok, kolor):
    kolor = "#" + kolor
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill() 

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

with io.open ("obraz.txt", "r", encoding="utf8") as myfile:
    data = myfile.read().splitlines()
    

startx = -400
starty = 400
liczniky = 1

tracer(0,1)
for wiersz in data:
    #print(wiersz)
    move(startx, starty - 10 * liczniky)
    kolory = wiersz.split()
    licznikx = 1
    for k in kolory:
        rgb = k[1:-1]
        rgb = rgb.split(",")
        for i in range(len(rgb)):
            rgb[i] = int(rgb[i])
        move(startx + 10 * licznikx, starty - 10 * liczniky)
        kwadrat(10, rgb_to_hex((rgb[0], rgb[1], rgb[2])))
        licznikx += 1
    
    liczniky += 1

done()