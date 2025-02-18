import io

with io.open ("slowapal.txt", "r", encoding="utf8") as myfile:
    data = myfile.read().splitlines()


def czy_palindrom(wyraz1, wyraz2):
    return  wyraz1 + wyraz2 == (wyraz1 + wyraz2)[::-1]


def najdluzszy_palindrom(slowa):
    palindromy = []
    for i in slowa:
        for j in slowa:
            if czy_palindrom(i, j):
                palindromy.append([i, j, len(i + j)])

    maxi = max(palindromy, key=lambda item:item[2])
    #print(palindromy)
    return [j[0] + " " + j[1] for j in palindromy if len(j[0] + j[1]) == maxi[2]]


print(najdluzszy_palindrom(data))