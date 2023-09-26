#왼쪽부터 차례로 다른 계란을 쳐서 최대한 많은 계란 깨는 경우
#계란으로 계란을 칠 시, 내구도= 내구도-상대무게
#처음에 내구성 max인 상대계란을 치려했으나, 반례 존재
#백트래킹으로 모든 경우 확인하면서 게란 많이 깨는 경우 max 갱신
import sys
input = sys.stdin.readline

def BackTracking(start):
    global Answer

    if start==N:
        total=0
        for i in range(N):
            if egg[i][0]<=0:
                total+=1

        Answer=max(Answer,total)
        return

    if egg[start][0]<=0:
        BackTracking(start+1)
        return

    check=True
    for i in range(N):
        if i==start:
            continue
        if egg[i][0]>0:
            check=False
            break

    if check: #다 깨져있는 경우
        Answer=max(Answer , N-1) #자기빼고 전부다니깐 N-1
        return

    for i in range(N):
        if i==start or egg[i][0]<=0:
            continue
        egg[start][0]-=egg[i][1]
        egg[i][0]-=egg[start][1]
        BackTracking(start+1)
        egg[start][0]+=egg[i][1]
        egg[i][0]+=egg[start][1]

N=int(input())
egg=[list(map(int,input().split())) for _ in range(N)] #내구도와 무게
Answer=0
BackTracking(0)

print(Answer)


