##

import math

def fun(x):
    fx = 4046 * (math.sqrt(x ** 14 + 1) - 1) / x ** 14

    return fx 

print(fun(0.001))
print("")

for i in range(1, 10):
    print(fun(1 / 10 ** i))
print("")

##

def poprawneFun(x):
    fx = 4046 * 1 / ((math.sqrt(x ** 14 + 1)) + 1)

    return fx


print(poprawneFun(0.001))
print("")

for i in range(1, 10):
    print(poprawneFun(1 / 10 ** i))