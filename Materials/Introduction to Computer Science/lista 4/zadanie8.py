from wdi import *

n = input("podaj liczbe ")
m = input("podaj liczbe ")
D = len(n)

A = Array(D)
B = Array(D)

X = Array(10)
Y = Array(10)

for i in range(D):
    A[i] = int(n[i])
    B[i] = int(m[i])

for i in range(D):
    X[A[i]] += 1
    Y[B[i]] += 1

czyjest = True

for i in range(10):
    if X[i] != Y[i]:
        czyjest = False
        break

if czyjest:
    print("jest podobna")
else:
    print("nie jest podobna")

