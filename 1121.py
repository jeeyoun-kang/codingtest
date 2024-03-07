def solution(n):
    # 5개씩 담을 수 있는 최대한의 5로 나눈 몫
    max_5_boxes = n // 5

    # 5로 나눈 나머지가 0일 경우 해당 상자 개수를 리턴
    if n % 5 == 0:
        return max_5_boxes

    # 5의 배수가 되지 않는 경우, 3개씩 담을 수 있는 최대한의 3으로 나눈 몫
    while max_5_boxes >= 0:
        remainder = n - (max_5_boxes * 5)
        if remainder % 3 == 0:
            return max_5_boxes + (remainder // 3)
        max_5_boxes -= 1

    # 옷을 담을 수 없는 경우 -1 리턴
    return -1


# 테스트 예시
print(solution(15))  # 결과: 3
print(solution(7))  # 결과: -1