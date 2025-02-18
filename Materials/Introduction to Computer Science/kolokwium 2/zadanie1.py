def wylicz(n, m):
    if m==0:
        return n

    if n ==0:
        return m

    if n%2==0:
        k = n/2
    else:
        k = (n+1)/2
    print(k, m-1)
    print(n-1, 1)
    return wylicz(k,m-1) + wylicz(n-1, 1) +1



wylicz(2,3)