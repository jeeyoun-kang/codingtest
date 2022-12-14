N=int(input())
P=list(map(int,input().split()))
P.sort()
count=0
M=N
for i in range(N):

    count+=P[i]*M
    M+=-1

print(count)