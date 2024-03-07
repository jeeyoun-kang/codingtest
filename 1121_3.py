def solution(maps):
    if not maps:
        return 0

    rows, cols = len(maps), len(maps[0])
    max_length = 0
    visited = [[0 for _ in range(cols)] for _ in range(rows)]

    def dfs(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols or maps[row][col] != 1 or visited[row][col]:
            return 0

        visited[row][col] = 1

        length = 4
        if row > 0 and maps[row - 1][col] == 1:
            length -= 1
            length += dfs(row - 1, col)
        if col > 0 and maps[row][col - 1] == 1:
            length -= 1
            length += dfs(row, col - 1)
        if row < rows - 1 and maps[row + 1][col] == 1:
            length -= 1
            length += dfs(row + 1, col)
        if col < cols - 1 and maps[row][col + 1] == 1:
            length -= 1
            length += dfs(row, col + 1)

        return length

    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 1 and not visited[i][j]:
                max_length = max(max_length, dfs(i, j))

    return max_length

# 테스트
maps1 = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1]
]
maps2 = [
    [1, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 0, 0]
]
print(solution(maps1))  # 예상 출력: 16
print(solution(maps2))  # 예상 출력: 10
