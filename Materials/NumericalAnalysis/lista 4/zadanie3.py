def definicja(a, b, f):
    mid = (a + b) / 2

    if (f(mid) > 0):
        a, b = a, mid
    elif (f(mid) < 0):
        a, b = mid, b

    return [a, b, mid]

def fun(x):
    fx = x - 0.49

    return fx

def bisekcja(a0, b0, f):
    x0 = 0.49

    for i in range(0, 6):
        b = definicja(a0, b0, f)

        a0 = b[0]
        b0 = b[1]
        mid = b[2]

        print(abs(mid - x0))

bisekcja(0, 1, fun)