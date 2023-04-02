import sys
input = sys.stdin.readline
n = int(input())
answer = []
for i in range(n):
    answer.append(list(map(int,input().split())))
answer.sort()
for j in answer:
    print(*j)