#고속도로 위에 최대 K개의 집중국
#N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야한다.
#이 상황에서 각 집중국의 수신 가능영역의 거리의 합의 최솟값

#정렬된 집중국 리스트에서 인접한 집중국간 간격을 리스트에 대입
#내림자순 정렬 후,k-1만큼 pop(0)

import sys
input = sys.stdin.readline

n=int(input()) #센서
k=int(input()) #집중국
arr=list(map(int,input().split()))
arr.sort()

if k>=n:
    print(0)
    exit()
result=[]
for i in range(1,n):
    result.append(arr[i]-arr[i-1])
result.sort(reverse=True)
for i in range(k-1):
    result.pop(0)
print(sum(result))