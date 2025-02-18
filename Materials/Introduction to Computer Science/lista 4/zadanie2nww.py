from wdi import *

n = int(input("podaj liczbe "))
m = int(input("podaj liczbe "))

z = n
y = m

ln = 1
lm = 1

while n != m:
    if n > m:
        m = y * lm
        lm += 1
    else:
        n = z * ln
        ln += 1

print(n , m)