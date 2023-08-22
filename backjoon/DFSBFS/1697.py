import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
def bfs():
    queue = deque([N])
    while queue:
        bfs_v = queue.popleft()
        if bfs_v == K:
            print(visited[bfs_v])
            break
        for a in (bfs_v - 1, bfs_v + 1, bfs_v * 2):
            if 0 <= a <= 100000 and not visited[a]:
                visited[a] = visited[bfs_v] + 1  # 노드에 이동시간 표시
                queue.append(a)


visited = [0] * (100001)
bfs()