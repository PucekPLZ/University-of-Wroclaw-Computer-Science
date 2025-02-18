n = int(input("podaj liczbe calkowita "))
k = int(input("podaj ilosc bitow "))
licznik = 1

N = [0] * k

if n < 0:
    n = n * -1

    while n > 0:
        if n % 2 == 0:
            N[-licznik] = 0
        else:
            N[-licznik] = 1

        licznik += 1
        n = n // 2

    for i in range(len(N)):
        if N[i] == 0:
            N[i] = 1
        else:
            N[i] = 0

    for i in range(1, len(N)):

        if N[-i] == 0:
            N[-i] = 1
            break
        else:
            N[-i] = 0

    print(N)
else:
    while n > 0:
        if n % 2 == 0:
            N[-licznik] = 0
        else:
            N[-licznik] = 1

        licznik += 1
        n = n // 2

    print(N)




