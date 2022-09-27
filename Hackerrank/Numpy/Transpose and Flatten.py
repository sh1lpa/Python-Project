import numpy

val = input('')
n,m = [eval(i) for i in val.split(' ')]
# print(n,m)
matrix = numpy.empty([n,m], dtype=int )
for i in range(n):
    cols = [int(i) for i in (input().split(' '))]
    for index, col in enumerate(cols):
        matrix[i][index] = col

print(matrix.transpose())
print(matrix.flatten())