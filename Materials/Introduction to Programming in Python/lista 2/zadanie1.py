n = 4
k = 5
    

for i in range(n*2):
    if i % 2  == 0:
        for i in range(k):
            for i in range(2*n):
                if i == 2*n -1:
                    if i % 2 == 0:
                        print(" " * k)
                    else:
                        print("#" * k)
                else:
                    if i % 2 == 0:
                        print(" " * k, end="")
                    else:
                        print("#" * k, end="")
    else:
        for i in range(k):
            for i in range(2*n):
                if i == 2*n -1:
                    if i % 2 == 1:
                        print(" " * k)
                    else:
                        print("#" * k)
                else:
                    if i % 2 == 1:
                        print(" " * k, end="")
                    else:
                        print("#" * k, end="")


