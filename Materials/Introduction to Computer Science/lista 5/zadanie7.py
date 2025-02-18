def potnr(a, b):
    rez = 1
    while b>0:
        if b%2:
            rez = rez * a

        b = b // 2
        a = a * a
        
    return rez

def liczba(n, m):
    k = 1
    while potnr(n, k) < m:
        k += 1

    return k

print(liczba(2, 16))