import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = [0]
total = 0
for i in range(len(arr)):
    total += arr[i]
    result.append(total)

for _ in range(M):
    i, j = map(int, input().split())
    print(result[j] - result[i - 1])