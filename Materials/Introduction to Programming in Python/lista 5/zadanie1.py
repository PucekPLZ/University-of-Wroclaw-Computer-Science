import statistics

def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None

def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def wywolanie(n):
    ciag = []
    x = n
    ciag.append(n)
    while x != 1:
        ciag.append(F(x))
        x = F(x)
    
    return ciag

def energia(n):
    return n.index(1)

def analiza_collatza(a, b):
    energie = []
    
    for i in range(a, b+1):
        energie.append(energia(wywolanie(i)))
    
    srednia = sum(energie)/len(energie)
    mediana = median(energie)
    maximum = max(energie)
    minimum = min(energie)

    return srednia, mediana, maximum, minimum

""" for i in range(7, 15):
    print(wywolanie(i)) """

#print(energia(wywolanie(7)))

print(analiza_collatza(7, 20))

    

