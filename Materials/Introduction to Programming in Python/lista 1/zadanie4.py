from losowanie_fragmentow import losuj_fragment

def haslo(n):
    zmienna = n
    tablice = []
    while zmienna != 0:
        slowo = losuj_fragment()
        dlugosc = len(slowo)
        if zmienna - dlugosc != 1:
            if zmienna > dlugosc:
                tablice.append(slowo)
                zmienna = zmienna - dlugosc
            elif zmienna == dlugosc:
                tablice.append(slowo)
                zmienna = zmienna - dlugosc

    return tablice

for i in range(10):
    print("".join(haslo(8)))
    print("")
    lista1 = haslo(12)
    print("".join(haslo(12)))
    print("")
    
