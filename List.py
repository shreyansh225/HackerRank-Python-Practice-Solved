if __name__ == '__main__':
    N = int(input())
    list1 = []
for i in range(N):
    stri = input().split()
    if(stri[0] == "print"):
        print(list1)
    elif(stri[0] == "sort"):
        list1.sort()
    elif(stri[0] == "pop"):
        list1.pop()
    elif(stri[0]=="insert"):
        list1.insert(int(stri[1]),int(stri[2]))
    elif(stri[0]=="remove"):
        list1.remove(int(stri[1]))
    elif(stri[0]=="append"):
        list1.append(int(stri[1]))
    elif(stri[0]=="reverse"):
        list1.reverse()
