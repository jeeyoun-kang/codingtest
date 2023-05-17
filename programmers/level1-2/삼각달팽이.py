n=int(input())
result = [[0] * n for _ in range(n)]
answer = []
a, b = -1, 0
num = 1

for i in range(n):
    for j in range(i, n):
        # 아래
        if i % 3 == 0:
            a += 1
        # 오른쪽
        elif i % 3 == 1:
            b += 1
        # 위쪽 대각선
        elif i % 3 == 2:
            a -= 1
            b -= 1

        result[a][b] = num
        num += 1

for i in range(n):
    for j in range(n):
        if result[i][j]==0:
            continue
        answer.append(result[i][j])