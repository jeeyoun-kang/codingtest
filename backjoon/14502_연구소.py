#벽을 3개 세우기
from sys import stdin
n,m = list(map(int,stdin.readline().split()))
lab = []
for i in range(n):
    lab.append(stdin.readline().split())
print(lab)