def pythagorean(n):
    return [(a,b,c) for a in range(n) for b in range(a, n) for c in range(b, n) if a**2+b**2==c**2 and a >0 and b >0 and c>0]

def primes(n):
    return [x for x in range(2, n+1) if all(x % y != 0 for y in range(2, x))]

def flatten(n):
    return [(n[a][b]) for a in range(len(n)) for b in range(len(n[a]))]

def transpose(m):
    return [[m[b][a] for b in range(len(m))] for a in range(len(m[0]))]



L = 20

T = [[2,3,4],[234,234,43],[34,23,4]]

M = [[1,2], 
     [4,3], 
     [5,6]]


print(pythagorean(L))
print(primes(L))
print(flatten(T))
print(transpose(M))