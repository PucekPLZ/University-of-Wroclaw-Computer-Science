import math

def RombergMethod(n, m, b, a, f):
    if n == 0 and m == 0:
        return 1/2 * (b - a) * (f(a) + f(b))
    if m == 0:
        sum = 0
        for x in range(0, 2**n):
            sum += f(a + 2 * (x - 1) * ((b - a) / 2**n))
        return 1/2 * RombergMethod(n - 1, 0, b, a, f) + (b - a) / (2**n) * sum
    else:
        return RombergMethod(n, m - 1, b, a, f) + (1 / (4 * m - 1)) * (RombergMethod(n, m - 1, b, a, f) - RombergMethod(n - 1, m - 1, b, a, f))

def fun1(x):
    return 2024 * x**8 - 1977 * x**4 - 1981

def fun2(A):
    return 1 / (1 + A ** 2)

def fun3(B):
    return math.sin(5 * B - (math.pi / 3))

for m in range(0, 21):
    for k in range(0, m - 1):
        print(RombergMethod(m, k, 2, -3, fun1))