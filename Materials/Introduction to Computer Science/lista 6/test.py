def ftrec(n, k):
    if n >= 0 and k == 0:
        return n
    elif k >= 0 and n == 0:
        return k
    else:
        return ftrec(n-1, k-1) + ftrec(n, k-1) + 1


print(ftrec(10,6))