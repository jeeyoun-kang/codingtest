#우선순위 큐를 이용한 프림 알고리즘
import heapq
import collections
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # 행성의 수
graph = collections.defaultdict(list) # 빈 그래프 생성
visited = [0] * (n+1) # 노드의 방문 정보 초기화

#그래프 생성
for i in range(1,n+1): # 간성 정보 입력 받기
    a=list(map(int,input().split()))
    for j in range(1,n+1):
        graph[i].append([a[j-1],i,j])

# 프림 알고리즘
def prim(graph, start_node):
    visited[start_node] = 1 # 방문 갱신
    candidate = graph[start_node] # 인접 간선 추출
    heapq.heapify(candidate) # 우선순위 큐 생성
    mst = [] # mst
    total_weight = 0 # 전체 가중치

    while candidate:
        weight, u, v = heapq.heappop(candidate) # 가중치가 가장 적은 간선 추출
        if visited[v] == 0: # 방문하지 않았다면
            visited[v] = 1 # 방문 갱신
            mst.append((u,v)) # mst 삽입
            total_weight += weight # 전체 가중치 갱신

            for edge in graph[v]: # 다음 인접 간선 탐색
                if visited[edge[2]] == 0: # 방문한 노드가 아니라면, (순환 방지)
                    heapq.heappush(candidate, edge) # 우선순위 큐에 edge 삽입

    return total_weight

print(prim(graph,1))
