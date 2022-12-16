from sys import stdin
N = int(stdin.readline().rstrip())
A = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
X = list(map(int,stdin.readline().split()))
for i in X:
    print(1) if i in A else print(0)
