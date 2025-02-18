import turtle

przekantna = (2 ** 0.5) / 2


t = turtle.Turtle()
t.setheading(45)

for i in range(20, 101, 10):
    t.penup()
    t.goto(i/2, -i/2)
    t.pendown()
    t.circle(i * przekantna, steps=4)


turtle.done()