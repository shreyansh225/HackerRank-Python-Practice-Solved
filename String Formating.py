def print_formatted(n):
    width = len("{0:b}".format(n))
    [print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width = width)) for i in range(1, n + 1)]

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
# d-decimal
# o-octal
# X-hexadecimal
# b-binary    
    
#...................................................OR...................................................


"""
def print_formatted(N):
    width = len(bin(N)[2:])
    for i in range(1, N + 1):
        print(' '.join(map(lambda x: x.rjust(width), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
"""
   
