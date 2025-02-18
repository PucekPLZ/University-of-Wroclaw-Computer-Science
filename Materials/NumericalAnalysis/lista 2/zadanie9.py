##

import math

def fun(n):
    xk = [2]
    
    for k in range(1, n):
        xk.append(2 ** k * math.sqrt(2 * (1 - math.sqrt(1 - (xk[k-1] / 2 ** k) ** 2))))
    
    return xk

z = fun(40)
for i in range(len(z)):
    print(z[i])
print("")

##

def poprawneFun(n):
    xk = [2]

    for k in range(1, n):
        xk.append(xk[k-1] * math.sqrt(2 / (1 + math.sqrt(1 - (xk[k-1] / 2 ** k) ** 2))))

    return xk

z = poprawneFun(40)
for i in range(len(z)):
    print(z[i])