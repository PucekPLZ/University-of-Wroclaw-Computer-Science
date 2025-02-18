def fun(N, A, B):
    if N == 0:
        return [[]]
    else:
        return [str(x) + y for x in range(A, B+1) for y in fun(N-1, x, B)]


print(fun(2,1,5))