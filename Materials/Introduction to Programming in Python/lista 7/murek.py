from turtle import *


def kwadrat(bok):
    begin_fill()
    for i in range(4):
      fd(bok)
      rt(90)
    end_fill()
    
def murek(s,bok):
  for a in s:
     if a == 'f':
         kwadrat(bok)
         fd(bok)
     elif a == 'b':
         kwadrat(bok)
         fd(bok)         
     elif a == 'l':
         bk(bok)
         lt(90)
     elif a == 'r':
        rt(90)
        fd(bok)
     elif a == 'y':
        fillcolor("yellow")
     elif a == 'p':
        fillcolor("purple")
        
color('black', 'yellow')

ht()

tracer(0,0) # szybkie rysowanie     
#murek('fffffffffrfffffffffflfffffffffrfffffl',10)    
#murek(4 * 'fffffr', 14)   
n = 7
for i in range(n):
    if i == 0:
        murek("yb", 10)

    murek("pfyb"*(n//2), 10)

    if i % 2 == 0:
        if i != n-1:
            murek("r", 10)
            murek("pf", 10)
            murek("r", 10)
        else:
            murek("r", 10)
    else:
        if i != n-1:
            murek("l", 10)
            murek("yb", 10)
            murek("l", 10)
        else:
            murek("l", 10)

penup()
goto(-90, -90)
pendown()

for i in range(10):
    murek("yfpb"* (i+1), 10)
    murek("r", 10)

update() # uaktualnienie rysunku
input()
