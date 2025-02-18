from turtle import *

speed("fastest")
right(30)
shape('triangle')

def trojkat(dlugosc, glebokosc):
    if glebokosc == 0:
        pd()
        stamp()
        pu()
        return
    else:
        pu()
        for i in range(0,3):
            forward(dlugosc)
            trojkat(dlugosc/2, glebokosc-1)
            backward(dlugosc)
            left(120)
        

trojkat(200, 5)
done()