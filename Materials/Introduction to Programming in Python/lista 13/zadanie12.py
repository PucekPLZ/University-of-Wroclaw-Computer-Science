import turtle

def pentagon(bok, pow):
    turtle.left(36)
    if pow == 0:
        turtle.forward(bok)
        turtle.left(72)
    else:
        pentagon(bok, pow - 1)
        turtle.forward(bok)
        turtle.left(72)
        

pentagon(100, 4)
turtle.done()
