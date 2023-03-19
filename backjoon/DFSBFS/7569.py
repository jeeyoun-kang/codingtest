# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램
from collections import deque
import sys
input = sys.stdin.readline

# 너비 우선 탐색
def bfs(x, y):
    # 이동할 여섯 가지 방향 정의 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dz = [-1,1]
    # deque 생성
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽이므로 진행 불가
            if graph[nx][ny] is None:
                continue

            # 벽이 아니므로 이동
            else:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
        # 위 아래 방향 위치 확인
        for j in range(2):
            nx = x
            ny = y+dz[j]*N

            # 위치가 벗어나면 안되기 때문에 조건 추가
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽이므로 진행 불가
            if graph[nx][ny] is None:
                continue

            # 벽이 아니므로 이동
            else:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 마지막 값에서 카운트 값을 뽑는다.
    return graph[N - 1][M - 1]


graph = []
M,N,h = map(int,input().split())
for i in range(N):
    for k in range(h):
        a = list(map(int,input().split()))
        graph.append(a)

