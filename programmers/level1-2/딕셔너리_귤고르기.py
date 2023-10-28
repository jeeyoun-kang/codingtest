from collections import Counter


def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine) #counter함수는 따로 어떠한 것을 기준삼아 정렬을 해주는것이 아니여서 따로 정렬이 필요!
    # {3: 2, 2: 2, 5: 2, 1: 1, 4: 1}
    sort_ = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    print(sort_)
    # 정렬된 딕셔너리로 귤 개수 맞추기
    cnt = 0
    for i in sort_:
        k -= i[1]
        answer += 1

        if k <= 0:
            break

    return answer