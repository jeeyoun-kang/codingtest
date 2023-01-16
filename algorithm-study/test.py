# DFS 함수 정의
import sys
input = sys.stdin.readline
n = int(input())
graph=[[] for _ in range(n+1)]
for i in range(n):
    a,b,c=map(int,input().split())
    graph[a].append(b,c)
print(graph)
# def dfs(graph, v, visited):
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#             # 만약 방문하지 않은 노드가 있다면
#         if not visited[i]:
#                 # 탐색 시작
#             dfs(graph, i, visited)
#
# # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# graph = [
#   [],        # 0을 기준으로 연결되어 있는 노드
#   [2, 3, 8], # 1을 기준으로 연결되어 있는 노드
#   [1, 7],
#   [1, 4, 5],
#   [3, 5],
#   [3, 4],
#   [7],
#   [2, 6, 8],
#   [1, 7]
# ]
#
# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# visited = [False] * 9
#
# # 탐색 시작 노드 1을 넣어주며 dfs() 실행
# dfs(graph, 1, visited)