def lp(n):
    i = 2
    F = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            F.append(i)
    if n > 1:
        F.append(n)
    
    F = [*set(F)]

    return F

print(lp(1111))


