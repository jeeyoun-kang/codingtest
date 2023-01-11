import sys
n,m = map(int,sys.stdin.readline().split())
land = [[0]*m for _ in range(n)]
for i in range(n):
    land[i]=list(map(int,sys.stdin.readline().split()))

