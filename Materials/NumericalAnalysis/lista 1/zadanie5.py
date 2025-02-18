import math

In = [math.log(2024/2023)]

for n in range(1, 20):
    In.append(1/n - 2023 * In[n-1])

for i in range(len(In)):
    print(In[i])