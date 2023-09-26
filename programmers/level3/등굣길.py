# 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return

#bfs
from collections import deque
dx = [0, 1]
dy = [1, 0]

def solution(m, n, puddles): # Y,X,물잠긴좌표
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    queue = deque()
    queue.append([0, 0])
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if [ny + 1, nx + 1] in puddles:
                    continue
                dp[nx][ny] += dp[x][y]
                if (nx, ny) not in queue:
                    queue.append([nx, ny])
    answer = dp[n - 1][m - 1] % 1000000007
    return answer

#dp
def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for i, j in puddles:
        dp[j][i] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:  # 웅덩이이면
                dp[i][j] = 0  # dp 더한 값에 영향을 주지 않게 하기 위해 0으로 바꾸고
                continue  # 건너뜀

            # 위에서 오는 경우와 왼쪽에서 오는 경우를 더해줌
            dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return (dp[n][m])