def selectionSort(array, n):
    l = 0
    for ind in range(n):
        min_index = ind
 
        for j in range(ind + 1, n):

            if array[j] < array[min_index]:
                min_index = j
            l+=1
            print(array)
        (array[ind], array[min_index]) = (array[min_index], array[ind])
    print(l)
    return array

arr = [7,6,5,4,3,2,1,0]
size = len(arr)

print(selectionSort(arr, size))