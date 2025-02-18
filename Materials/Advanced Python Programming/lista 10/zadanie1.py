import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import sys
import time

def generate_squares():
    while len(squares) < num_squares:
        square = (random.randint(1, size - 1), random.randint(1, size - 1))

        if square not in squares and square not in snake:
            squares.add(square)

def starting_snake():
    square_snake = (random.randint(2, size - 2), random.randint(2, size - 2))
    snake.append(square_snake)

    flag = True
    head = snake[0]

    while flag:
        square_snake = (random.randint(head[0] - 1, head[0] + 1), random.randint(head[1] - 1, head[1] + 1))

        if square_snake != head and (square_snake[0] == head[0] or square_snake[1] == head[1]):
            snake.append(square_snake)

            flag = False

def next_snake():
    head = snake[-1]
    flag = True

    while flag:
        square_snake = (random.randint(head[0] - 1, head[0] + 1), random.randint(head[1] - 1, head[1] + 1))

        if (square_snake != head and square_snake != snake[-2]
            and (square_snake[0] == head[0] or square_snake[1] == head[1])
            and square_snake[0] > 0 and square_snake[1] > 0
            and square_snake[0] < size and square_snake[1] < size):

            snake.append(square_snake)

            if len(snake) > 7:
                snake.pop(0)

            flag = False

def end_game():
    head = snake[-1]

    if head in snake[:-1] or head in squares:
        time.sleep(2)
        sys.exit()

def update(frame):
    ax.clear()

    for i in range(size + 1):
        plt.plot([i, i], [0, size], color='black', linestyle='-', linewidth=1)
        plt.plot([0, size], [i, i], color='black', linestyle='-', linewidth=1)

    for square in squares:
        plt.fill_between([square[0], square[0] + 1], square[1], square[1] + 1, color='red')

    for segment in snake:
        plt.fill_between([segment[0], segment[0] + 1], segment[1], segment[1] + 1, color='green')

        if segment == snake[-1]:
            plt.fill_between([segment[0], segment[0] + 1], segment[1], segment[1] + 1, color='blue')

    end_game()
    next_snake()

size = 20
num_squares = 7
snake = []  
squares = set()

fig, ax = plt.subplots()
ax.set_xlim(0, size)
ax.set_ylim(0, size)
ax.set_aspect('equal', 'box')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

starting_snake()
generate_squares()

ani = animation.FuncAnimation(fig, update, frames=200, interval=200)

plt.show()