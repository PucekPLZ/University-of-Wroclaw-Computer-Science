import math
import numpy 

def fun(x):
    fx = 14 * (1 - math.cos(17 * x)) / x ** 2

    return fx

for i in range(11, 20):
    print(fun(10 ** -i))
print("")

for i in range(11, 20):
    print(numpy.float32(fun(10 ** -i)))