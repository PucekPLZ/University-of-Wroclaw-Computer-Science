def lista():
    A = {v for i in range (1,10) for j in range (0,10) for k in range (0,10)
         for v in [i*10**9+j*100000000+k*10000000+7777777,i*1000000000+j*100000000+77777770+k,i*1000000000+777777700+10*j+k,7777777000+i*100+j*10+k,7777777000+j*10+k]}
    #print(len(A))
    return A


def pierwsza(n):
    i = 2
    while i * i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

#print(tabela())

def s():
    return sorted([p for p in lista() if pierwsza(p)])


x = s()
print(len(x),x)