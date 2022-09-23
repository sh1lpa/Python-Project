import numpy

val = input('')
n,m,p = [eval(i) for i in val.split(' ')]
# print(n,m)
matrix1= numpy.empty([n,p], dtype=int )
matrix2= numpy.empty([m,p], dtype=int )
for i in range(n+m):
    cols = [int(i) for i in (input().split(' '))]
    for index, col in enumerate(cols):
        # print(index)
        if i < n:
            matrix1[i][index] = col
        else:
            matrix2[i-n][index] = col
print(numpy.concatenate((matrix1, matrix2), axis=0))