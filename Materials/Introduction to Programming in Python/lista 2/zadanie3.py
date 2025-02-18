import math

def kolko(n, p=0):

    sx = n/2
    sy = n/2
    r = n/2
    zmienna = 0
    #print(r**2)
    for i in range(n):
        print(" " * p , end="")
        y = i+0.5
        zmienna = y
        for j in range(n):
            
            x = j+0.5
            #print((x-sx)**2+(y-sy)**2)
            if (x-sx)**2+(y-sy)**2<=r**2:
                if j == n-1:
                    print("*")
                else:
                    print("*", end="")
            else:
                if j == n-1:
                    print(" ")
                else:
                    print(" ", end="")

            
            

kolko(7, 4)
kolko(9, 3)
kolko(15)



        