#언어: pypy3
from sys import stdin
N,K = list(map(int,stdin.readline().split()))
coin=[0]*N
coinnum=0
count=0
for i in range(N):
    coin[i]=int(stdin.readline())

for j in range(len(coin)):
    if K<coin[j]:
        coinnum+=j-1
        break

if coinnum==0: #K보다 높은 숫자가 없을때
    coinnum += coin.index(max(coin))

while(K!=0):

    if K>=coin[coinnum]:
        K-=coin[coinnum]

        count+=1
    if K<coin[coinnum]:
        coinnum+=-1

print(count)


