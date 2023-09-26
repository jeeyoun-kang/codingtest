# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return
def solution(m, n, puddles):  # Y,X,물잠긴좌표
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    def dfs(a, b):  # Y,X
        dx = [0, 1]
        dy = [1, 0]
        for i in range(2):
            ny = dy[i] + a
            nx = dx[i] + b

            if 0 <= nx and nx <= n and 0 <= ny and ny <= m:
                for j in range(len(puddles)):
                    if ny != puddles[j][1] or nx != puddles[j][0]:
                        dp[nx][ny] += 1
                        dfs(ny, nx)

    dfs(1, 1)
    print(dp)
    return dp[n][m] % 1000000007