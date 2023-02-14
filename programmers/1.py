# #은 선이고 .은 선안에 둘러싸여있어야 포함된다.
def solution(grid):
    answer = 0
    return answer

grid=[".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."]

# 이동할 8 가지 방향 정의 (상, 하, 좌, 우,대각선)
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def dfs(x,y):

    for j in range(8):
        nx = 0
        ny = 0
        nx = x + dx[j]
        ny = y + dy[j]
        # 미로 찾기 공간을 벗어난 경우 무시
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
            continue


result = 0
for i in range(len(grid)): # #만 더하고 + . 위치 파악후 더하기
    count=[]
    for k in range(len(grid[0])):
        if grid[i][k]=="#":
            result+=1
        else:
            dfs(i,k)




print(result)

