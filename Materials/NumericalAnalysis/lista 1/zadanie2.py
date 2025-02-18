import math

def fun(x):
    fx = 4046 * (math.sqrt(x ** 14 + 1) - 1) / x ** 14

    return fx 

print(fun(0.001))
print("")