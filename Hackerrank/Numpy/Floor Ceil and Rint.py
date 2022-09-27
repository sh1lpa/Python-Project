import numpy 
numpy.set_printoptions(legacy='1.13')
A = [float(i) for i in input().split()]
print(f'{numpy.floor(A)}\n{numpy.ceil(A)}\n{numpy.rint(A)}')