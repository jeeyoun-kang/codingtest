# 네트워크 개수 리턴(간접 네트워크도 하나로 취급)

#파이썬 기본적 재귀한도는 1000 > Recursion Error 생각
#노드가 수만이면 아래 세팅, 수십만이면 BFS로 풀이
import sys
sys.setrecursionlimit(10**6) #100만으로 늘리기

def solution(n, computers):
    answer = 0
    def dfs(x):
        visited[x] = 1
        for i in range(n):
            if computers[x][i] == 1 and not visited[i]:
                dfs(i)   # 연결된 애로 파고들어감

    visited = [0] * n

    for i in range(n):
        if not visited[i]:   # 새 덩어리 발견
            dfs(i)           # 이 덩어리 통째로 방문 처리
            answer += 1
            
    return answer

#클로드버전 - BFS
from collections import deque
def solution(n, computers):
    visited = [0] * n
    answer = 0
    for start in range(n):
        if not visited[start]:
            q = deque([start])
            visited[start] = 1
            while q:
                x = q.popleft()
                for i in range(n):
                    if computers[x][i] == 1 and not visited[i]:
                        visited[i] = 1
                        q.append(i)
            answer += 1
    return answer


solution([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
