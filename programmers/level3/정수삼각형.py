def solution(triangle):
    triangle.reverse()

    # 두개의 아래 리스트의 값들중 하나 + 위 리스트의 값의 합이 최대일때
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):  # 아래 리스트만큼
            triangle[i][j] = max(triangle[i - 1][j] + triangle[i][j], triangle[i - 1][j + 1] + triangle[i][j])
    return int(*triangle[len(triangle)-1])