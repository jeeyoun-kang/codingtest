# # 도착 최단 갯수 return, 방법없을시 -1
# def solution(maps):
#     n, m = len(maps), len(maps[0])
#     visited = [[False] * m for _ in range(n)]
#     answer = [-1]   # 결과 담을 곳

#     def dfs(x, y, dist):
#         # 범위 밖 / 벽 / 이미 방문 → 중단
#         if x < 0 or x >= n or y < 0 or y >= m:
#             return
#         if maps[x][y] == 0 or visited[x][y]:
#             return

#         # 도착: 지금까지 최단이면 갱신
#         if x == n - 1 and y == m - 1:
#             if answer[0] == -1 or dist < answer[0]:
#                 answer[0] = dist
#             return

#         visited[x][y] = True           # 방문 표시

#         dfs(x + 1, y, dist + 1)        # 상하좌우 (대각선 X)
#         dfs(x - 1, y, dist + 1)
#         dfs(x, y + 1, dist + 1)
#         dfs(x, y - 1, dist + 1)

#         visited[x][y] = False          # 백트래킹: 방문 해제

#     dfs(0, 0, 1)
#     return answer[0]
      

#클로드 버전 - BFS
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]      # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((0, 0, 1))    # (x, y, 지금까지 이동 칸 수)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while q:
        x, y, dist = q.popleft()

        if x == n - 1 and y == m - 1:   # 도착점 꺼내는 순간이 최단
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:                    # 맵 범위 안
                if maps[nx][ny] == 1 and not visited[nx][ny]:  # 길이고 미방문
                    visited[nx][ny] = True                     # 넣을 때 바로 방문 표시
                    q.append((nx, ny, dist + 1))

    return -1   # 큐 다 비면 도착 실패


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
