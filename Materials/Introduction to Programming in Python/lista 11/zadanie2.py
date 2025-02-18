def liczby(napis):
    dd = {}

    po = ""
    l = 1
    for i in range(len(napis)):
        if napis[i] in dd.keys():
            po += dd[napis[i]]
            if i != len(napis)-1:
                po += "-"
        else:
            dd[napis[i]] = str(l)
            l += 1
            po += dd[napis[i]]
            if i != len(napis)-1:
                po += "-"
    
    return po



print(liczby("napis"))
print(liczby("kajak"))
print(liczby("indianin"))