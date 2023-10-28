def solution(order):
    answer = 0
    tmp = []  # 임시 컨테이너
    i = 1  # [1,2,3,4,5] 기존 순서 유지

    while i != len(order) + 1:
        tmp.append(i)
        while tmp[-1] == order[answer]:
            answer += 1
            tmp.pop()
            if len(tmp) == 0:  # 임시컨테이너가 쌓인게 없으면 모두 택배에 넣은것!
                break
        i += 1
    return answer