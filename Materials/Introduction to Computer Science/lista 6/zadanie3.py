def bubbleSort(arr):
    n = len(arr)

    swapped = False
    
    for i in range(n-1):

        for j in range(n-1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
    
        if not swapped:
            return arr
   
    return arr
 
arr = [7, 6, 5, 4, 3, 2, 1]
 
print(bubbleSort(arr))