def nwd(a, b):
    c = a + b

    while c > 0:
        if a % c == 0 and b % c == 0:
            return c
        c -= 1
    return 1

def ulamek(a, b) :
     
    d = nwd(a, b);
 
    a = a // d;
    b = b // d;
 
    return a, b

a = int(input("podaj liczbe "))
b = int(input("podaj liczbe "))

print(ulamek(a, b))

