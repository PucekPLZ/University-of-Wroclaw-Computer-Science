import io

with io.open ("popularne_slowa.txt", "r", encoding="utf8") as myfile:
    data = set(myfile.read().splitlines())


for slowo in data:

    przesuniecia = []
    przesuniete_slowo = slowo
    for i in range(len(slowo)-1):
        przesuniete_slowo = przesuniete_slowo[1:]
        litera = slowo[i]
        przesuniete_slowo = przesuniete_slowo + litera

        if przesuniete_slowo in data:
            przesuniecia.append(przesuniete_slowo)

    if len(przesuniecia) > 1:
        s = ' '.join(przesuniecia)
        print(slowo, s)
