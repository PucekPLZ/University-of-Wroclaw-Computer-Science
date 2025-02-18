import turtle

kolory = ["#FFCCFF", "#FF99FF", "#FF66FF", "#FF33FF", "#FF00FF", "#CC00CC", "#990099"]

t = turtle.Turtle()
t.setheading(45)
t.speed(50)

for i in range(14):
    if i % 2 == 0:
        t.fillcolor(kolory[i//2])

    for j in range(i+1):
        t.begin_fill()
        t.circle(12, steps=4)
        t.end_fill()

        t.penup()
        t.right(45)
        t.forward(16)
        t.left(45)
        t.pendown()

    t.penup()
    t.left(135)
    t.forward(16)
    t.right(225)
    t.pendown()

        



turtle.done()
