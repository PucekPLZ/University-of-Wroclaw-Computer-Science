def sito(n):
    L = [0] + n * [1]
    p = 2
    q = p * p
    while q <= n:
        if L[p] == 1:  
            i = q
            while i <= n:  
                L[i] = 0
                i = i + p
        p = p + 1
        q = p * p
    M = []
    for i in range(1, n+1):
        if L[i] == 1:
            M.append(i)
        else:
            M.append(0)
    return M

def palindromy(a, b):
    Z = sito(b)
    T = []

    for i in range(a, b+1):
        j = str(i)
        if i in Z and j == j[::-1]:
            T.append(i)

    return T

print(palindromy(11, 900))
