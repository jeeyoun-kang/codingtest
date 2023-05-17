
def draw(x, y, cnt, num):
    if cnt < 1:
        return

    number = num
    for i in range(cnt):
        arr[x + i][y] = number
        number += 1
    for i in range(1, cnt):
        arr[x + cnt - 1][y + i] = number
        number += 1
    for i in range(1, cnt - 1):
        arr[x + cnt - 1 - i][y + cnt - 1 - i] = number
        number += 1
    draw(x + 2,y + 1, cnt - 3, number)


n=int(input())
arr = [[0] * n for _ in range(n)]
draw(0, 0, n, 1)

answer = []
for i in range(n):
    for j in range(i + 1):
        answer.append(arr[i][j])
print(answer)