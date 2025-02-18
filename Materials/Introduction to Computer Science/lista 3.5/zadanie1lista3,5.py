x = [1,1,1,0,1,1,1,0]
y = [0,0,0,0,1,1,1,0]

z = 0
for i in range(len(x)):
    if z == 0:
        if x[-i-1] + y[-i-1] == 0:
            x[-i-1] = 0
        elif x[-i-1] + y[-i-1] == 1:
            x[-i-1] = 1
        else:
            x[-i-1] = 0
            z = 1
    else:
        if x[-i-1]+y[-i-1]+z == 1:
            x[-i-1] = 1
            z = 0
        elif x[-i-1]+y[-i-1]+z == 2:
            x[-i-1] = 0
            z = 1
        else:
            x[-i-1] = 1
            z = 1

print(z, x)