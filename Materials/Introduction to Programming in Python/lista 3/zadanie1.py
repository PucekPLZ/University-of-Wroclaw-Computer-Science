from traceback import print_tb


def pierwsza(n):
    i = 2
    while i * i <= n:
        if n%i == 0:
            return False
        i += 1
    return True


k = [n for n in range(1, 100001)]

licznik = 0

for i in range(len(k)):
    s = str(k[i])

    if pierwsza(k[i]):
        if "7" * 3 in s:
            print(k[i])
            licznik += 1

print("Takich liczb jest", licznik)


