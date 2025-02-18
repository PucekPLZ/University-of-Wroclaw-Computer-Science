def silnia(n):
    
    for i in range(n):
        silnia = 1
        for j in range(i+1):
            silnia = silnia * (j+1)
        
    return silnia

def dlugosc(liczba):

    d = str(liczba)
    l = len(d)

    return(l)

def odmiana(cyfry):
    slowo = ""
    if cyfry == 1:
        slowo = "cyfre"
    elif cyfry <= 14 and cyfry >= 12 or cyfry >= 112 and cyfry <= 114:
        slowo = "cyfr"
    elif cyfry % 10 == 2 or cyfry % 10 == 3 or cyfry % 10 == 4:
        slowo = "cyfry"
    else:
        slowo = "cyfr"
    
    return slowo

for i in range(100):
    #print(silnia(i+1))
    #print(dlugosc(silnia(i+1)))
    #print(odmiana(dlugosc(silnia(i+1))))
    #print(i+1)
    print(f"{i+1}! ma {dlugosc(silnia(i+1))} {odmiana(dlugosc(silnia(i+1)))}")
    print("")




