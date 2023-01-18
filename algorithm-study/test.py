
import sys
input = sys.stdin.readline

n = int(input())

loc = [0 for _ in range(n+1)]
per = [0 for _ in range(n+1)]
dis = 0  # 사람*위치 합친 거리
count=0 # 사람 수만 합친 수
test=0
result=[0 for _ in range(n+1)]
for i in range(n):
    x,a = map(int,input().split())
    loc[x]=x
    per[x]=a

for j in range(1,n+1): #각 마을별 비용 구하기
    for k in range(1,n+1):
        test+=abs(k-j)*per[k]
    result[j]=test
    test=0
result.pop(0)
print(result.index(min(result))+1)



