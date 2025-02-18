def wartosc(a,k):
    w=0
    for i in range(k):
        w = w + a[i]*pot(2,k-i-1)
    return w

def pot(a, b):
    rez = 1
    while b>0:
        if b%2:
            rez = rez * a
        b = b // 2
        a = a * a
    return rez


a = [1, 0 , 1 , 1, 0]
k = len(a)

print(wartosc(a, k))