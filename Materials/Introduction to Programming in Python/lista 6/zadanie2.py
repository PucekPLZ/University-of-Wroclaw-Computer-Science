import io

def odwrot(s):
    return s[::-1]

def usun(slowa):
    wynik = set()

    for e in slowa:
        if odwrot(e) in slowa and odwrot(e) not in wynik and e not in wynik:
            wynik.add(e)

    return wynik

def wypisz(wynik):
    for e in wynik:
        print(e, " ", odwrot(e))



with io.open ("popularne_slowa.txt", "r", encoding="utf8") as myfile:
    data = set(myfile.read().splitlines())


print(wypisz(usun(data)))
