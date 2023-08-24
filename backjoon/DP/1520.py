import sys
input = sys.stdin.readline

def dfs(x,y):

    if x ==m-1 and y==n-1: # 도착지점에 왔다면 1 리턴해 이동한 모든칸에 1을 더한다
        return 1

    if dp[x][y]==-1: #이동시마다 0으로 방문설정
        dp[x][y]=0

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and map[x][y]>map[nx][ny]:
                dp[x][y]+=dfs(nx,ny)

    return dp[x][y] # 방문칸일때 dp값 리턴




m,n = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(dfs(0,0))