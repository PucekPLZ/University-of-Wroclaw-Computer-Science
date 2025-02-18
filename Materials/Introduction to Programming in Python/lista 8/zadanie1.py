import random
from collections import defaultdict as dd
import io
import re

with io.open ("brown.txt", "r", encoding="utf8") as myfile:
    brown = myfile.read().split()

pol_ang = dd(lambda:[])

for x in open('pol_ang.txt'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue    
    pol, ang = L
    pol_ang[pol].append(ang)

def ilosc(slowo):
    T = []
    #print(pol_ang[slowo])
    for i in pol_ang[slowo]:
        T.append(brown.count(i))

    #print(T)
    m = max(T)
    ind = T.index(m)

    return ind

def tlumacz(polskie):
    wynik = []
    for s in polskie:
        if s in pol_ang:
            maximum = ilosc(s)
            wynik.append(pol_ang[s][maximum])
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()
zdanie2 = 'chłopiec lubić grać w gry'.split()

print(tlumacz(zdanie))  
print(tlumacz(zdanie2))  

            

