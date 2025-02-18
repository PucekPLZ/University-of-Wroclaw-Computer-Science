from wdi import *

def ile_czynnikow(n):
    z = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            z += 1
    if n > 1:
        z += 1
    return z

def czynniki(n, d):
    x = 0
    C = Array(d)
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            C[x] = i
            x += 1
    if n > 1:
        C[x] = n
    return C

n = int(input("podaj liczbe "))

for i in range(ile_czynnikow(n)):
    print(czynniki(n, ile_czynnikow(n))[i], " ", end="")







