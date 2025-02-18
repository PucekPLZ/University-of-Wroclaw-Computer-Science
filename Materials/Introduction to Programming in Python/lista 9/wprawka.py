zbior = {1,2,3}

def dodawanie(a,b):
    x = a + b
    z = "%s + %s = %s" % (a,b,x)
    l = [z,x]
    return l

def odejmowanie(a,b):
    x = a - b
    z = "%s - %s = %s" % (a,b,x)
    l = [z,x]
    return l

def dzielenie(a,b):
    x = a / b
    z = "%s / %s = %s" % (a,b,x)
    l = [z,x]
    return l

def mnozenie(a,b):
    x = a * b
    z = "%s * %s = %s" % (a,b,x)
    l = [z,x]
    return l


for i in zbior:
    for j in zbior:
        if i == dodawanie(i,j)[1] or j == dodawanie(i,j)[1] :
            print(dodawanie(i,j)[0])

        if i == odejmowanie(i,j)[1] or j == odejmowanie(i,j)[1] :
            print(odejmowanie(i,j)[0])
        
        if i == dzielenie(i,j)[1] or j == dzielenie(i,j)[1] :
            print(dzielenie(i,j)[0])

        if i == mnozenie(i,j)[1] or j == mnozenie(i,j)[1] :
            print(mnozenie(i,j)[0])

