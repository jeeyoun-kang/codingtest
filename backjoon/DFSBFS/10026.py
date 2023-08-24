import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = list(input().strip() for _ in range(n))
visited = [[0]*n for _ in range(n)]
cnt_1=0 # 정상인 사람이 봤을때 구역 수
cnt_2=0 # 적록색약인 사람이 봤을때 구역 수
def bfs(a,b):
    dx = [-1,+1,0,0]
    dy = [0,0,-1,+1]
    queue = deque()
    queue.append([a,b])
    visited[a][b]=1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and arr[x][y]==arr[nx][ny]: #같은 색깔일때
                visited[nx][ny]=1
                queue.append([nx, ny])

    return

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt_1+=1

visited = [[0]*n for _ in range(n)]


for i in range(n):
    arr[i] = arr[i].replace('R','G')


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt_2 += 1

print(cnt_1,end=' ')
print(cnt_2)

