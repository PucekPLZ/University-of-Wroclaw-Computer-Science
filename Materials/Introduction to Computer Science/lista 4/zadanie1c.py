from wdi import *

n = int(input("podaj liczbe "))
x = int(input("podaj liczbe "))

suma = 0
potega = 1
for i in range(n):
    for j in range(i+1):
        potega = potega 
    suma += (i+1) * x ** (i+1)

