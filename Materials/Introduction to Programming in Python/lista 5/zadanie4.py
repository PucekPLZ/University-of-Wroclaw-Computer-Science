def klucz(e):
    return e[1]

def usun_duplikaty(n):
    L2 = []

    for i in range(len(n)):
        L2.append([0,0])

    for i in range(len(n)):
        L2[i][0] = n[i]
        L2[i][1] = i

    L2 = sorted(L2)
    L3 = []

    for i in range(1, len(L2)):
        if L2[i-1][0] == L2[i][0]:
            L3.append(L2[i])

    for i in range(len(L3)):
        L2.remove(L3[i])

    L2 = sorted(L2, key=klucz)

    return L2

n = [4,3,2,1,4,5,4,6,6,7]

print(usun_duplikaty(n))


