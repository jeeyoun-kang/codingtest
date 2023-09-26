def solution(n):
    answer = [0, 1]
    for i in range(2, n + 1):
        answer.append((answer[i - 1] + answer[i - 2]) % 1234567)

    return answer[-1]

# 재귀함수 구현시 stackoverflow가 터지기에 for문으로 구현