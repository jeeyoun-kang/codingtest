from sys import stdin


n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
lis = [0]

for case in a:
    if lis[-1]<case:
        lis.append(case)
    else:
        left = 0
        right = len(lis)

        while left<right:
            mid = (right+left)//2
            if lis[mid]<case:
                left = mid+1
            else:
                right = mid
        lis[right] = case

print(len(lis)-1)

#bisect 이용방법
import bisect
import sys

input = sys.stdin.readline
x = int(input())
arr = list(map(int, input().split()))

temp = [arr[0]]

for i in range(x):
    if arr[i] > temp[-1]:
        temp.append(arr[i])
    else:
        idx = bisect.bisect_left(temp, arr[i])
        temp[idx] = arr[i]

print(len(temp))
