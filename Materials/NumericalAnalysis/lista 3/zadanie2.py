import math

def metoda_szkolna(a, b, c):
    x1 = (-b - math.sqrt(b ** 2 - 4 * a * c))/ 2 * a

    x2 = (-b + math.sqrt(b ** 2 - 4 * a * c))/ 2 * a

    return x1, x2

for i in range(11, 20):
    wynik = metoda_szkolna(1, 10 ** i, 1)

    print(wynik[0], " " * (25 - len(str(wynik[0]))), wynik[1])

print("")

for i in range(11, 20):
    wynik = metoda_szkolna(1, -10 ** i, 1)

    print(wynik[0], " " * (25 - len(str(wynik[0]))), wynik[1])

##
print("")

def poprawione(a, b, c):
    if b < 0:
        x1 = 2 * c / (-b + math.sqrt(b ** 2 - 4 * a * c)) 

        x2 = (-b + math.sqrt(b ** 2 - 4 * a * c))/ 2 * a

    elif b >= 0:
        x1 = (-b - math.sqrt(b ** 2 - 4 * a * c))/ 2 * a

        x2 = 2 * c / (-b - math.sqrt(b ** 2 - 4 * a * c)) 

    return x1, x2
    

for i in range(11, 20):
    wynik = poprawione(1, 10 ** i, 1)

    print(wynik[0], " " * (25 - len(str(wynik[0]))), wynik[1])

print("")

for i in range(11, 20):
    wynik = poprawione(1, -10 ** i, 1)

    print(wynik[0], " " * (25 - len(str(wynik[0]))), wynik[1])