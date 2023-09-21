# 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return
# 도착 할수 없을때는 -1 return
# 최단거리구해야되기에 bfs로 풀기
from collections import deque


def solution(maps):
    def bfs(x, y):
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque()
        queue.append([x, y])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx and nx <= len(maps) - 1 and 0 <= ny and ny <= len(maps[0]) - 1 and maps[nx][ny] == 1:
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append([nx, ny])

    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = 1
    bfs(0, 0)
    if visited[len(maps) - 1][len(maps[0]) - 1] == 0:
        return -1
    else:
        return visited[len(maps) - 1][len(maps[0]) - 1]