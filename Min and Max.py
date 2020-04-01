import numpy
N, M = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(A, axis=1), axis=0))

"""
Input Format

The first line of input contains the space separated values of N and M.
The next N lines M contains  space separated integers.

Output Format

Compute the min along axis 1 and then print the max of that result.

Sample Input

4 2
2 5
3 7
1 3
4 0
Sample Output

3
Explanation

The min along axis 1  = [2,3,1,0]
The max of [2,3,1,0] = 3
"""
