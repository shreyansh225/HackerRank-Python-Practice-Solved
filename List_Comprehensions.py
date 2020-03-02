if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

result= []
p = 0 
for i in range(x+1):
    for j in range(y+1): 
        for k in range(z+1):
            if i+j+k != n: 
                result.append([])
                result[p] = [ i, j, k]
                p+=1 
print(result)                

#=================OR======================OR===================OR======================OR=================
#=================OR======================OR===================OR======================OR=================

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if((i+j+k) != n)])
