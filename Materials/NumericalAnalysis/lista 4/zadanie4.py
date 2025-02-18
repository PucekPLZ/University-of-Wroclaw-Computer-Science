import math

def definicja(a, b, f):
    mid = (a + b) / 2

    if (f(mid) > 0):
        a, b = a, mid
    elif (f(mid) < 0):
        a, b = mid, b

    return [a, b, mid]

def fun(x):
    fx = x ** 4 - math.log(x + 4)

    return fx

def bisekcja(a0, b0, f):
    err = abs((b0 + a0) / 2)

    while (err > 10 ** -8):
        err = err / 2
        b = definicja(a0, b0, f)

        a0 = b[0]
        b0 = b[1]
        mid = b[2]

    return mid

print(bisekcja(0, -3, fun))
print("")
print(bisekcja(0, 100, fun))