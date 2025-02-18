import io
import re

with io.open ("popularne_slowa.txt", "r", encoding="utf8") as myfile:
    slowapl = set(myfile.read().splitlines())

with io.open ("lalkapierwszytom.txt", "r", encoding="utf8") as myfile:
    lalka = myfile.read()

    lalka = re.findall(r"[\w]+|[,.!?-]", lalka)
 
    #print(lalka)

znakipl = ["ą","ę","ź","ć","ń","ś","ó","ł"]
znaki = [",", "?", "!", "-", "."]

tekst = []
dlugosc = 0

dlugi_tekst = []
max_dlugosc = 0
for slowo in lalka:
    czy_dodane = False
    zpl = True
    if slowo in slowapl:
        for i in slowo:
            if i in znakipl:
                zpl = False
                break
            
        if zpl:
            tekst.append(slowo)
            czy_dodane = True
            if slowo not in znaki:
                dlugosc += len(slowo)
    
    if czy_dodane:
        if dlugosc > max_dlugosc:
            max_dlugosc = dlugosc
            dlugi_tekst = tekst
    else:
        dlugosc = 0
        tekst = []

    #print(dlugosc, tekst)

d = " ".join(dlugi_tekst)
print(d)


            
