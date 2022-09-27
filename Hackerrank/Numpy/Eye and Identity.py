import numpy
numpy.set_printoptions(legacy='1.13')
val = input('')
n,m = [eval(i) for i in val.split(' ')]
print(numpy.eye(n,m))