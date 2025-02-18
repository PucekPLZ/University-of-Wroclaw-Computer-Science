def sum(L):
    if not L:
        return set([0])
    else:
        s = sum(L[1:])
        return set([x + L[0] for x in s]) | s


print(sorted(sum([1,2,3,100])))