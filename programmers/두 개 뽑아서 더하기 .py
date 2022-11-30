def solution(numbers):
    from itertools import combinations as cb

    answer = []

    for i, j in cb(numbers, 2):
        if i + j not in answer:
            answer.append(i + j)

    return sorted(answer)