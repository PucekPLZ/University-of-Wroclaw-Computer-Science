y = [1, -1/9]

for i in range(2, 50):
    y.append((80 / 9 * y[i-1]) + y[i-2])

for i in range(len(y)):
    print(y[i])