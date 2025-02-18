n = 12


for i in range(n*2+1):
    if i == 0 or i == n*2:
        print("*"*(n*2+1))
    elif i == n:
        print("*", end="")
        print(" " * (n-1), end="")
        print("*", end="")
        print(" " * (n-1), end="")
        print("*")
    elif i == 1 or i == n*2 - 1:
        print("*" * 2, end="")
        print(" "* (n*2-3), end="")
        print("*" * 2)
    elif i <= n:
        print("*", end="")
        print(" " * (i-1), end="")
        print("*", end="")
        print(" " * ((n-i)+(n-i-1)), end="")
        print("*", end="")
        print(" " * (i-1), end="")
        print("*")
    else:
        print("*", end="")
        print(" " * (2*n-1-i), end="")
        print("*", end="")
        print(" " * ((i-n)+(i-n-1)), end="")
        print("*", end="")
        print(" " * (2*n-1-i), end="")
        print("*")
            




        