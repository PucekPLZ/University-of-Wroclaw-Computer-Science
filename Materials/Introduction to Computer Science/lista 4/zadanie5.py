from wdi import *

n = input("podaj liczbe ")
D = len(n)
A = Array(D)
B = Array(D)

for i in range(D):
    A[i] = n[i]

zmienna = D-1

for i in range(D):
    B[i] = A[zmienna]
    zmienna = zmienna - 1

czyjest = True

for i in range(D):
    if A[i] != B[i]:
        czyjest = False
        break

if czyjest:
    print("jest palindromem binarnym")
else:
    print("nie jest palindromem binarnym")

    
        
    

