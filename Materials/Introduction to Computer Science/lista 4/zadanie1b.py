from wdi import *

n = int(input("podaj liczbe "))

suma = 0
for i in range(n):
    suma += (-1)**(i+1)/(i+1)

print(suma)