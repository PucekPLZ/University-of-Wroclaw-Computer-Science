def obliczanie(N, K):
    if K == 1:
        return {N}
    elif K == 2:
        return {N+N, N-N, N*N, N/N}
    else:
        wynik = set()
        for i in range(1, K):
            for a in obliczanie(N, i):
                for b in obliczanie(N, K-i):
                    wynik.add(a+b)
                    wynik.add(a-b)
                    wynik.add(a*b)
                    if b != 0:
                        wynik.add(a/b)
        return wynik


print(obliczanie(4,2))