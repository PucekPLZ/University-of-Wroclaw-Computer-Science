def podziel(n):
    flaga = True

    k = ""
    slowa1 = []
    slowa2 = []
    for i in range(len(n)):
        if n[i] == " ":
            flaga = False
            slowa1.append(k)
            k = ""
        else:
            flaga = True

        if flaga:
            k += n[i]
    slowa1.append(k)

    for i in range(len(slowa1)):
        if not slowa1[i] == '':
            slowa2.append(slowa1[i])

    return slowa2


s = "ala ma kota    adfsdf     "

print(podziel(s))

