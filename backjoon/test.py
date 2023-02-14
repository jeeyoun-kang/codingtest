import sys
input = sys.stdin.readline

def dfs(r, c, idx, total): # 좌표,접근한 블럭갯수,값
    global ans
    #현 위치에서 남은 블록이 모두 최댓값에 해당하더라도 현재 ans를 넘기지 못하면 종료
    if ans >= total + max_val * (3 - idx): # 선택할 수 있는 남은 블럭의 갯수만큼 (3 - idx) 곱하기
        return
    # 3칸 모두 이동했을 시
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1: #"ㅗ"모양 : 기존 블럭에서 탐색하게 만듬
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + arr[nr][nc]) # 현 위치(r,c)에서 dfs 호출
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + arr[nr][nc]) # 다음 블록에서 dfs 호출
                visit[nr][nc] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, arr)) #arr 안에서 제일 큰 값

for r in range(N):
    for c in range(M):
        visit[r][c] = 1 #1로 만듬(방문)
        dfs(r, c, 0, arr[r][c])
        visit[r][c] = 0 #0으로 만듬(다른 좌표에서도 방문 가능하게 하기위해)

print(ans)