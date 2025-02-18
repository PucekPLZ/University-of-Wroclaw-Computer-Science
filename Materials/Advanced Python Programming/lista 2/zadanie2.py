def sudan(n, x, y):
    if n == 0:
        return x + y
    elif y == 0:
        return x
    else:
        return sudan(n - 1, sudan(n, x, y - 1), sudan(n, x, y - 1) + y)
    
def sudan_memo(n, x, y, memo={}):
    if (n, x, y) in memo:
        return memo[(n, x, y)]

    if n == 0:
        result = x + y
    elif y == 0:
        result = x
    else:
        result = sudan_memo(n - 1, sudan_memo(n, x, y - 1, memo), sudan_memo(n, x, y - 1, memo) + y)

    memo[(n, x, y)] = result
    return result

# najwieksze argumenty dla wersji bez spamiętywania sudan(1, 25, 25)
print(sudan(1, 20, 20))
print("")

# najwieksze argumenty dla wersji ze spamiętywaniem 
# dla n = 1 sudan_memo(1, 950, 950), dla n = 2 sudan_memo(2, 5, 2)
print(sudan_memo(2, 5, 2))