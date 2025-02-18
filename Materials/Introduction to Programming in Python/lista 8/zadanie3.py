from collections import defaultdict as dd
import io

with io.open ("popularne_slowa.txt", "r", encoding="utf8") as myfile:
    slowapl = set(myfile.read().splitlines())

def slownikliter(slowo):
    slownik = dd(lambda:"")

    litery = []
    slowo = slowo.lower()
    for i in slowo:
        if i != " ":
            litery.append(i)

    for i in range(len(slowo)):
        if slowo[i] not in slownik and slowo[i] != " ":
            slownik[slowo[i]] = litery.count(slowo[i])

    return slownik
        
def ukladalne(slowo, slowo2):
    litery = []

    for i in slowo:
        litery.append(i)
    
    for i in range(len(slowo)):
        c = litery.count(slowo[i])

        if slowo[i] in slownikliter(slowo2):
            if c > slownikliter(slowo2)[slowo[i]]:
                return False 
        else:
            return False
        
    return True

imienazwisko = "Bolesław Prus"
sprawdzane = ''

po = set()
zbior = set()
for s in slowapl:
    if ukladalne(s, imienazwisko):
        zbior.add(s)
        litery = []
        imienazwisko = imienazwisko.lower()
        for i in imienazwisko:
            if i != " ":
                litery.append(i)

        for j in range(len(s)):
            if s[j] in litery:
                litery.remove(s[j])
        
        slowo = "".join(litery)
        z = s + " " + slowo
        po.add(z)

lista = []
for slowo in po:
    slowo = slowo.split()
    
    for j in zbior:
        if len(j) == len(slowo[1]):
            if ukladalne(j, slowo[1]):
                if len(slowo[0]) >= len(j):
                    x = slowo[0] + " " + j
                    lista.append(x)
                else:
                    x = j + " " + slowo[0]
                    lista.append(x)
                
    #print(slowo)

L = []
for j in range(len(lista)):
    if lista[j] not in L:
        L.append(lista[j])

for j in range(len(L)):
    print(L[j])

#print(imienazwisko)

#print(slownikliter(imienazwisko))

