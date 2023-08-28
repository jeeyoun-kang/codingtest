import sys
input = sys.stdin.readline
# n은 3*2^k 의 수 (3, 6, 12, 24, 48, ...) (0 ≤ k ≤ 10, k는 정수)
n = int(input())
arr = ["  *  ", " * * ", "*****"]
n = n//3

def recursion(arr):
    arr_size = len(arr)
    for i in range(arr_size):
        arr.append(arr[i] + " " + arr[i])
        arr[i] = " "*arr_size+ arr[i] + " "*arr_size

    return arr

cnt = 0
while n > 1:
    n //= 2
    cnt += 1

for i in range(cnt):
    recursion(arr)

for arrs in arr:
    print(arrs)