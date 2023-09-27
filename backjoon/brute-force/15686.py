import sys
input = sys.stdin.readline
from itertools import combinations as cb
#0은 빈 칸, 1은 집, 2는 치킨집
# #r과 c는 1부터 시작
#치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
#도시의 치킨 거리는 모든 집의 치킨 거리의 합
#도시 치킨집중 최대 m개 고르고, 도시의 치킨거리가 가장 작게될지 구하기

n,m =map(int,input().split()) #도시 수,폐업시키지 않을 치킨집
arr = [list(map(int,input().split())) for _ in range(n)]
chicken=[]

def short(test):
    result=0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                nxny = 999
                for k in range(m):
                    a, b = test[k]
                    nx = abs(a-i)
                    ny = abs(b-j)
                    nxny=min(nxny,nx+ny)
                result+=nxny
    return result

for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            chicken.append([i,j])

test_chicken = list(cb(chicken,m))
# #폐업시키지 않을 치킨집 m개 경우의수
answer=999999
for test in test_chicken:
    a =short(test)
    answer = min(answer,a)
print(answer)
