from sys import stdin
N= int(stdin.readline())
test=[0]*N
for i in range(N):
    test[i]=int(stdin.readline())
test.sort()
for j in test:
    print(j)
