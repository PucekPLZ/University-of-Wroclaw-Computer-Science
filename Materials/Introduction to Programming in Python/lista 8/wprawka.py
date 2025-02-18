def tekstowa(N):

    x = str(N)
    tekst = ""

    if N >= 10 and N <= 20:
        tekst += liczby[N]
    else:
        for i in range(len(x)):
        
            if int(x[i]) != 0:
                if N >= 10 and N <= 20:
                    tekst += liczby[N]
                    break
                else:
                    z = int(x[i]) * 10 ** (len(x) - i - 1)
                    N = N % 100
        
                tekst += liczby[z]
                tekst += " "

    return tekst

def napis_z_liczbami(L):

    for i in range(len(L)):
        if str(L[i]) != L[i]:
            L[i] = tekstowa(L[i])
    
    t = ' '.join(L)

    return t


liczby = {
    1 : 'jeden',
    2 : 'dwa',
    3 : 'trzy',
    4 : 'cztery',
    5 : 'pięć',
    6 : 'sześć',
    7 : 'siedem',
    8 : 'osiem',
    9 : 'dziewięć',
    10 : 'dziesięć',
    11 : 'jedenaście',
    12 : 'dwanaście',
    13 : 'trzynaście',
    14 : 'czternaście',
    15 : 'piętnaście',
    16 : 'szesnaście',
    17 : 'siedemnaście',
    18 : 'osiemnaście',
    19 : 'dziewiętnaście',
    20 : 'dwadzieścia',
    30 : 'trzydzieści',
    40 : 'czterdzieści',
    50 : 'pięćdziesiąt',
    60 : 'sześćdziesiąt',
    70 : 'siedemdziesiąt',
    80 : 'osiemdziesiąt',
    90 : 'dziewięćdziesiąt',
    100 : 'sto',
    200 : 'dwieście',
    300 : 'trzysta',
    400 : 'czterysta',
    500 : 'pięćset',
    600 : 'sześćset',
    700 : 'siedemset',
    800 : 'osiemset',
    900 : 'dziewięćset'
  }


print(tekstowa(217))

K = ["ala", "ma", 200, "kotow", "i", 67, "domow"]

print(napis_z_liczbami(K))