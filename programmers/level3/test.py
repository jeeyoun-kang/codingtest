n,m,x,y,r,c,k=3,4,2,3,3,1,5

cnt = 0  # 이동 수
result = [[[] for _ in range(m+1)]for _ in range(n+1)]


def dfs(x, y, cnt):
    if cnt == k and x==r and y==c:
        return result[r][c]
    dx = [1, -1, 0, 0]  # u,d,0,0
    dy = [0, 0, -1, 1]  # 0,0,l,r
    remain,path = k-cnt,abs(x-r)+abs(y-c)
    if remain<path or remain%2!=path%2:
        pass
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx <= n and ny >= 0 and ny <= m:
            if i == 0:
                result[nx][ny].append(['d'])
            elif i == 1:
                result[nx][ny].append(['u'])
            elif i == 2:
                result[nx][ny].append(['l'])
            else:
                result[nx][ny].append(['r'])
        else:
            continue
        dfs(nx, ny, cnt + 1)


print(dfs(x, y, cnt))
print(result)
