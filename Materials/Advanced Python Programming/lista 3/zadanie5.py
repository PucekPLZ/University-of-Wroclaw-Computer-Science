def max_sublist_sum(lista):
    max_sum = 0
    pair = (0, 0)

    for i in range(len(lista)):
        sum = 0

        for j in range(i, len(lista)):
            sum += lista[j]

            if max_sum < sum:
                max_sum = sum
                pair = (i, j)

    return pair

l = [1000, 1, 1, 2, 3, 4, 5, -20, 90, 1, 2, 3, -40, 4, 1, 100]

print(max_sublist_sum(l))