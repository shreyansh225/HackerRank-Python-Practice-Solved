import numpy
N , M = map(int,input().split())
numpy.set_printoptions(legacy='1.13')
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.mean( A, axis = 1))
print(numpy.var( A, axis = 0))
print(numpy.std( A, axis = None))

"""
Input (stdin)
2 2
1 2
3 4

Expected Output
[ 1.5  3.5]
[ 1.  1.]
1.11803398875
"""
