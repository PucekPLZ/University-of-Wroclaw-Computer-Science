import math

def fun(x, a):
    fx = x - math.sqrt(a)

    return fx

def newton(x0, f, a):
    x = []

    x1 = x0 - fun(x0, a) 
    x.append(x1)

    for n in range(1, 10):
        xn = x[n-1] - f(x[n-1], a)
        x.append(xn)
        
    return x

wynik = newton(1, fun, 0.875 * 2 ** 3) # 7

for i in range(len(wynik)):
    print(wynik[i])