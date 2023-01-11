import sys
input = sys.stdin.readline

N = int(input())
ch2 = [0]*(N+1)

for i in range(N):
    a,b,c = map(int,input().split())
    ch2[a] = c

t = 1
cnt = -1
while True:
    t = ch2[t]
    cnt += 1
    if t == -1:
        break


print((N-1)*2 - cnt)