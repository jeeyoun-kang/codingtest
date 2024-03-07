def solution(bricks):
    if not bricks or len(bricks) < 3:
        return 0

    n = len(bricks)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = bricks[0]
    right_max[-1] = bricks[-1]

    # 왼쪽에서의 최대 높이 계산
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], bricks[i])

    # 오른쪽에서의 최대 높이 계산
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], bricks[i])

    # 물이 고일 수 있는 최대 높이 계산
    total_water = 0
    for i in range(n):
        water = min(left_max[i], right_max[i]) - bricks[i]
        if water > 0:
            total_water += water

    return total_water
print(solution([1, 2, 3, 4, 5, 6, 7]))