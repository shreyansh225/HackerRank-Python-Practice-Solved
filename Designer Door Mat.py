n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

""" 
used for string reverse 
eg: 
a="wills"
a[::-1]
will give:- "slliw"
 
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
.|..|..|..|..|..|..|.
-------WELCOME-------

here to print the lower part we need to print the upper region in reverse like this 

.|..|..|..|..|..|..|.
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
so pattern[ : :-1] is used since


pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
whih prints the upper region and pattern[ : :-1]prints the lower region 
"""
