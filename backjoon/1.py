import sys

n, m = map(int, sys.stdin.readline().split())
dot = sorted(list(map(int, sys.stdin.readline().split())))
for _ in range(m):
    left = 0
    right = n - 1
    x, y = map(int, sys.stdin.readline().split())
    while left <= right:
        mid=(left+right)//2
        if dot[mid] < x:
            left =mid+1
        else:
            right=mid-1
    firstIdx=left
    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2
        if dot[mid]>y:
            right=mid-1
        else:
            left=mid+1
    endIdx=right+1
    print(endIdx-firstIdx)