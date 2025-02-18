#1
def prefix(s, t):
    return s == t[:len(s)]

print(prefix("Ala ma kota", "Ala ma kota który jest gruby"))
print(prefix("Ala ma kota", "Kot ma Ale"))
print("")

#2
def drabina(L):
    return len(set(L)) == 2 and all([L[i] == L[i-2] for i in range(2,len(L))])

print(drabina([1,2,1,2,1,2,1]))
print("")

#3
def maleRybyWDuzych(L):
    return all(L[j] in L[i] for i in range(len(L)-1) for j in range(1, len(L)))

print(maleRybyWDuzych(['rekinisko', 'rekin', 'eki']))
print("")

#4
def sumaDlugosciABC(L):
    return sum([len(slowo) for slowo in L if all(x in 'abc' for x in slowo)])

print(sumaDlugosciABC(["baba", "ma", "kota", "a", "ty?"]))
print("")

#5
def poltaksowkowa(N):
    return any([(i**3 + j**3) == N for i in range(1, N) for j in range(i, N)])

print(poltaksowkowa(16))
