def sito(num):
    prime = [1 for i in range(num+1)]
# tablica 0 1
    p = 2
    while (p * p <= num):
  
        # jezeli prime[p] jest 1
        # jest pierwsza
        if prime[p] == 1:
  
            # potegi p
            for i in range(p * p, num+1, p):
                prime[i] = 0
        p += 1

    prime[0], prime[1] = 0, 0
    # drukowanie pierwszych
    for p in range(2, num+1):
        if prime[p] == 1:
            print(p)

    return prime

print(sito(20))