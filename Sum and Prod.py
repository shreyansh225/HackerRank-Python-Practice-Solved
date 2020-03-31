import numpy
N, M = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))

"""
Input (stdin)
2 2
1 2
3 4
Expected Output
24
"""
