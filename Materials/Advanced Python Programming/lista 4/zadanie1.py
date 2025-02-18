import timeit

def pierwsze_imperatywne(n):
    primes = []

    if n < 2:
        return primes
    
    for i in range(2, n + 1):
        prime = 2

        while prime <= i:
            if i % prime == 0:
                break

            prime += 1

        if prime == i:
            primes.append(i)

    return primes

def pierwsze_składane(n):
    return [i for i in range(2, n + 1) if all(i % j for j in range(2, i))]

def pierwsze_funkcyjne(n):
    return list(filter(lambda x: all(x % y != 0 for y in range(2, x)), range(2, n + 1)))

for i in range(10, 100, 10):
    if i == 10:
        print(" n" + "  " + "imperatywna" + "  " + "składana" + "  " + "funkcyjna")
    
    print(f"{i}:", end=" ")
    print(" " * 5 + str(timeit.timeit('pierwsze_imperatywne(i)', globals=globals(), number=10000))[:6], end=" ")
    print(" " * 3 + str(timeit.timeit('pierwsze_składane(i)', globals=globals(), number=10000))[:6], end=" ")
    print(" " * 4 + str(timeit.timeit('pierwsze_funkcyjne(i)', globals=globals(), number=10000))[:6])