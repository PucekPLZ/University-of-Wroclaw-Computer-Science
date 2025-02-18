import io

with io.open ("liczba mandatow.txt", "r", encoding="utf8") as myfile1:
    mandaty = myfile1.read().splitlines()

    for i in range(len(mandaty)):
        mandaty[i] = int(mandaty[i])

with io.open ("wynikipartii.txt", "r", encoding="utf8") as myfile2:
    wyniki = myfile2.read().splitlines()

    for i in range(len(wyniki)):
        wyniki[i] = wyniki[i].split()
        for j in range(len(wyniki[i])):
            wyniki[i][j] = float(wyniki[i][j])

def przypisanie_miejsc(w, m):
    ilorazy = []
    for i in range(len(w)):
        for j in range(1, m+1):
            ilorazy.append((w[i]/j, i))
    ilorazy.sort(key=lambda x: x[0], reverse=True)
    w_koncowy = [0] * len(w)
    for i in range(m):
        w_koncowy[ilorazy[i][1]] += 1
    return w_koncowy

M = []
for j in range(41):
    M.append(przypisanie_miejsc(wyniki[j], mandaty[j]))

ost = [0, 0, 0, 0, 0]

for wiersz in M:
    for i in range(5):
        ost[i] += wiersz[i]

print(ost)
        
