import io

with io.open ("popularne_slowa.txt", "r", encoding="utf8") as myfile:
    data = set(myfile.read().splitlines())


def rozne_litery(przeszukiwane_slowo, nastepne_slowo):
    r_litery = 0

    for i in range(len(przeszukiwane_slowo)):
        if przeszukiwane_slowo[i] != nastepne_slowo[i]:
            r_litery += 1
    
    if r_litery == 1:
        return True
    else:
        return False


def najkrotsza_sciezka(start, koniec, slowa):
    kolejka = [(start, [start])]

    odwiedzone = set()
    
    while kolejka:
        
        przeszukiwane_slowo, sciezka = kolejka.pop(0)

        if przeszukiwane_slowo == koniec:
            return sciezka

        odwiedzone.add(przeszukiwane_slowo)

        for nastepne_slowo in slowa:
            if rozne_litery(przeszukiwane_slowo, nastepne_slowo):
                if nastepne_slowo not in odwiedzone:
                    kolejka.append((nastepne_slowo, sciezka + [nastepne_slowo]))
                
    return []


start = "woda"
koniec = "wino"
slowa = set()

for slowo in data:
    if len(slowo) == 4:
        slowa.add(slowo)

print(najkrotsza_sciezka(start, koniec, slowa))
