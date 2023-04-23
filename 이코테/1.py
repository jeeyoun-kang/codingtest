import sys

input = sys.stdin.readline

t = int(input())
P = []
num_list = []
for i in range(t):
    P.append(input().strip())
    n = int(input())
    num_list.append(list(input()))
print(num_list)
