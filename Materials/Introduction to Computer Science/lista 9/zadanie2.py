def queens(n):
    licznik = 0
    b = [-1 for i in range(n)]
    b[0] = 0  # umieść pierwszego hetmana w „lewym dolnym” narożniku (na dole kolumny 0)
    k = 1  # przejdź do kolumny numer 1
    print(b)
    while k >= 0:
        
        print(b)
        # poszukiwanie „wolnego” pola w kolumnie k, idąc w górę od b[k]
        b[k] += 1
        if b[k] < n:
            if poprawne_ustawione(b, k):
                if k == n-1:
                    licznik += 1
                else:
                    k += 1
        else:
            b[k] = -1
            k -= 1
    return licznik


def poprawne_ustawione(a, k):
    i = 0
    while i < k:
        j = i + 1
        while j <= k:
            print(i, j)
            if a[i] == a[j] or a[i] - i == a[j] - j or a[i] + i == a[j] + j:
                return False
            j += 1
        i += 1
    return True


print(queens(4))
