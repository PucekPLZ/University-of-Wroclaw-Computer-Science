def palindroms(text):
    pairs = []

    for i in (range(len(text))):

        for j in range(i, len(text)):
            palindrom = text[i:j]

            if palindrom == palindrom[::-1] and len(palindrom) >= 2:
                pairs.append((i, j-i))

    return pairs

print(palindroms("adam kobylamamalybok sedes"))