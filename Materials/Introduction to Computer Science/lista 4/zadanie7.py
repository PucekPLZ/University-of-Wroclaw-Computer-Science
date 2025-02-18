from wdi import *

n = input("podaj liczbe ")
D = len(n)
A = Array(D)
B = Array(10)

for i in range(D):
    A[i] = int(n[i])

for i in range(D):
    B[A[i]] += 1

k = 0

for i in range(10):
    if B[i] > 0:
        k += 1
    
print(f"liczba {n} ma zapis {k} cyfrowy")
