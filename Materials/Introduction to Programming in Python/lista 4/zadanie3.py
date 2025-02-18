import random

def randperm(n) :

    Z = [] 
    L = [0] * n

    for i in range(n) :
        L[i] = i + 1
    
    # print(v)

    while (len(L)) :
        Z.append(randnum(L))
    
    return Z

def randnum(v) :

    index = random.randint(0, len(v) - 1)
    num = v[index]
 
    v[index], v[len(v) - 1] = v[len(v) - 1], v[index]
    v.pop()

    return num


print(randperm(9))
print(randperm(9))
print(randperm(9))
print(randperm(9))
     
#print(randperm(10 ** 6))