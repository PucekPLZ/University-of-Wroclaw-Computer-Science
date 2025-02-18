#1
def jednaWartosc(L):
    return len(set(L)) == 1

print(jednaWartosc([1,1,1,1,1,1]))
print(jednaWartosc([1,1,2,1,1,1]))
print("")

#2
def najwiekszaRoznica(L):
    return max([abs(L[i] - L[i+1]) for i in range(len(L)-1)])

print(najwiekszaRoznica([1,1,2,3,45,2,3]))
print("")

#3
def silnia(n):
    return 1 if n == 0 else n * silnia(n-1)

print(silnia(5))
print("")

#4
def sumaPodzielnychKwadratow(N, K):
    return sum([x**2 for x in range(1, N) if x % K == 0])

print(sumaPodzielnychKwadratow(8, 2)) 
print("")

#6
def posortowaneLeksyograficznie(L):
    return [int(x) for x in sorted(map(str, L))] #map zamienia liste na liste stringow, sortuje i poznej na int 

print(posortowaneLeksyograficznie([1,4,55,222,9,10])) 



