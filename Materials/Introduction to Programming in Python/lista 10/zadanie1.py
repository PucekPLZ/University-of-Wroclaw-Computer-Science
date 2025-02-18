def cezar(s, k):
    alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    przestawiony_alfabet = alfabet[k:] + alfabet[:k]
    zamiana = dict(zip(alfabet, przestawiony_alfabet))


    text = ''.join([zamiana[c] for c in s])

    return text


print(cezar("lucjan", 8))