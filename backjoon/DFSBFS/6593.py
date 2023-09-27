#각 변의 길이가 1인 정육면체(단위 정육면체)
#정육면체는 금으로 이루어져 있어(#) 지나갈 수 없거나, 비어있어서(.) 지나갈 수 있게 되어있다
#각 칸에서 인접한 6개의 칸(동,서,남,북,상,하)으로 1분의 시간을 들여 이동
#시작 지점은 'S'로 표현되고, 탈출할 수 있는 출구는 'E'
#각 층 사이에는 빈 줄이 있으며, 입력의 끝은 L, R, C가 모두 0으로 표현
#탈출시,Escaped in x minute(s).출력 ,x는 빌딩을 탈출하는 데에 필요한 최단 시간
#불가능, Trapped! 출력
import sys
input = sys.stdin.readline
from collections import deque
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(x,y,z):
    queue.append([x,y,z])
    time[x][y][z]=1
    while queue:
        x,y,z = queue.popleft() #x,y,z
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if build[nx][ny][nz] == 'E':
                    print("Escaped in {0} minute(s).".format(time[x][y][z]))
                    return
                if build[nx][ny][nz] == '.' and time[nx][ny][nz] == 0:
                    time[nx][ny][nz] = time[x][y][z] + 1
                    queue.append([nx, ny, nz])
    print("Trapped!")

while True:
    l, r, c = map(int, input().split())  # 빌딩층 수, 한층의 행, 열
    if l==0 and r==0 and c==0:
        break
    build = [[[] * c for _ in range(r)] for _ in range(l)]
    time = [[[0] * c for _ in range(r)] for _ in range(l)]
    queue = deque()
    for i in range(l):
        build[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if build[i][j][k] == 'S':
                    bfs(i, j, k)


