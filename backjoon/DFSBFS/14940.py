from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif arr[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1 # 현 위치 방문 값 + 1
                    queue.append((nx, ny))


for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            bfs(i, j)
# 반례 [[2,0],[0,0]]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()

