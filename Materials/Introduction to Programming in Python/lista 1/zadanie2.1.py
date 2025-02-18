import math


def silnia(n):
    
    for i in range(n):
        silnia = 1
        for j in range(i+1):
            silnia = silnia * (j+1)
        
        if silnia > 0:
            dlugosc = int(math.log10(silnia))+1
        elif silnia == 0:
            dlugosc = 1
        else:
            dlugosc = int(math.log10(-silnia))+2
            

        if dlugosc == 1:
            print(f"{i+1}! ma {dlugosc} cyfre")
        elif dlugosc <= 4:
            print(f"{i+1}! ma {dlugosc} cyfry")
        else:
            print(f"{i+1}! ma {dlugosc} cyfr")




silnia(100)