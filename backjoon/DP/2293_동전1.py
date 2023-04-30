n, k = list(map(int, input().split()))
c = []
dp = [0 for i in range(k + 1)]
dp[0] = 1 # 동전1개만 사용하는 경우의 수를 생각하기에
for i in range(n):
    c.append(int(input()))
for i in c:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]
print(dp[k])