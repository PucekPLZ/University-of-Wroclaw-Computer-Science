def potnr(a, b):
    rez = 1
    licznikm = 0
    while b>0:
        if b%2:
            rez = rez * a
            licznikm += 1
            print(a)
        b = b // 2
        a = a * a
        
    return rez

licznikm = 0
def potr(a, b, licznikm):
    
    
    if not b:
        return 1
    if b%2:
        licznikm += 1
        print(licznikm)
        return a*potr(a*a,b//2,licznikm)
    return potr(a*a,b/2,licznikm)
    

print(potnr(3, 3))

#print(potr(2, 1024, licznikm))
#print(potr(2, 2047, licznikm))


    




