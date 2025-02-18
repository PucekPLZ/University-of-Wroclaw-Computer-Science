def funkcja(A):
    max = 0
    for i in range(len(A)):
        suma = 0
        for j in range(i, len(A)):
            suma += A[j]

            if max < suma:
                max = suma


    return max


A = [-5,7,2,3,4,-2,1,1,1,-4]

print(funkcja(A))