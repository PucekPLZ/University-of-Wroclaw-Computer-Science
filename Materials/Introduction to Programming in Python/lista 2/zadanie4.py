from duze_cyfry import daj_cyfre


def dlc(tm):
    liczba = str(tm)
    liczba = list(liczba)
    dlugosc = len(liczba)

    for i in range(len(liczba)):
        liczba[i] = int(liczba[i])
    
    tablica = []
    licznik = 0

    for i in range(dlugosc):
        for j in daj_cyfre(int(liczba[i])):
            #print(j)
            tablica.insert(licznik, j)
            licznik += 1

    return tablica

def drukowanie(t):

    dlugosc = len(t)//5
    
    for i in range(5):
        for j in range(dlugosc):
            if j == dlugosc - 1:
                print(t[i+5*j], "")
            else:
                print(t[i+5*j], "", end="")
        

drukowanie(dlc(123))