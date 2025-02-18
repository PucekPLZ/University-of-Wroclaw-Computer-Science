def suma(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return suma(n-1)+suma(n-2)+suma(n-3)


print(suma(5))