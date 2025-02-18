from collections import defaultdict as dd

def slownikliter(slowo):
    slownik = dd(lambda:"")

    litery = []

    for i in slowo:
        litery.append(i)

    for i in range(len(slowo)):
        if slowo[i] not in slownik:
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

#print(slowikliter("kajak"))

print(ukladalne("kot", "lokomotywa"))
print(ukladalne("motyl", "lokomotywa"))
print(ukladalne("aktyw", "lokomotywa"))
print(ukladalne("kotka", "lokomotywa"))
print(ukladalne("paź", "lokomotywa"))
