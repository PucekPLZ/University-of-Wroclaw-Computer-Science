def kwadrat(n):
    zmienna = len(str(n))
    #print(zmienna)


    for i in range (n):
        print(" " * (zmienna-(len(str(i)))) + f"{i}" + " ", end="")
        if i == 0 or i == n-1:
            print("*" * n)
        else:
            print("*", end="")
            print("*" * (i-1), end="")
            print(" " * (n-2-i+1), end="")
            print("*")


kwadrat(123)        