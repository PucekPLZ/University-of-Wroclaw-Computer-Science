import turtle

def plotki(s):
    for i in range(20):
        t.fd(s)
        t.right(90)
        t.fd(7)
        t.right(90)
        t.fd(s)
        s = s - 2
        t.left(180)

def plotki2(s):
    for i in range(20):
        t.fd(s)
        t.left(90)
        t.fd(7)
        t.left(90)
        t.fd(s)
        s = s + 2
        t.right(180)


t = turtle.Turtle()
t.speed('fastest')


def pletwa():
    t.forward(140)
    t.right(90)
    plotki(42)
    t.right(180)
    plotki2(2)
    t.right(90)
    t.forward(140)


def wiatrak(n):
    for i in range(n//2):
        pletwa()
        t.right(360/n)

wiatrak(3)
turtle.exitonclick()
