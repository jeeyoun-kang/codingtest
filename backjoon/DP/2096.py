import sys
input = sys.stdin.readline

n = int(input())
# 메모리 제한으로 첫 줄 입력 값을 dp에 갱신
a, b, c = map(int, input().split())
dp_max = [[0] * 3 for _ in range(n)]
dp_min = [[0] * 3 for _ in range(n)]

dp_max[0] = [a,b,c]
dp_min[0] = [a,b,c]

for i in range(1, n):
    a, b, c = map(int, input().split())
    dp_max[i][0] = max(a + dp_max[i - 1][0], a + dp_max[i - 1][1])
    dp_max[i][1] = max(b + dp_max[i - 1][0], b + dp_max[i - 1][1], b + dp_max[i - 1][2])
    dp_max[i][2] = max(c + dp_max[i - 1][1], c + dp_max[i - 1][2])

    dp_min[i][0] = min(a + dp_min[i - 1][0], a + dp_min[i - 1][1])
    dp_min[i][1] = min(b + dp_min[i - 1][0], b + dp_min[i - 1][1],b + dp_min[i - 1][2])
    dp_min[i][2] = min(c + dp_min[i - 1][1], c + dp_min[i - 1][2])

max_result = max(dp_max[n - 1])
min_result = min(dp_min[n - 1])
print(max_result,min_result)