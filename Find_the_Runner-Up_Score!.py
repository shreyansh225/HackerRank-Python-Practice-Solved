if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    zes = max(arr)
    x=0
    while(x<n):
        if zes ==max(arr):
            arr.remove(max(arr))
        x+=1
    print(max(arr))
