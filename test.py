from collections import Counter


def solution(S):
    count = Counter(S)
    max_removal = float('inf')

    # "B", "A", "N"의 개수 중 가장 작은 값 구하기
    for char in "BAN":
        max_removal = min(max_removal, count[char])

    return max_removal


# 테스트
print(solution("NAABXXAN"))  # 1
print(solution("NAANAAXNABABYNNBZ"))  # 2
print(solution("QABAAAWOBL"))  # 0