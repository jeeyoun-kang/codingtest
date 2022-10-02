def solution(lottos, win_nums):
    answer = []
    count = 0
    question = 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                count += 1
    for k in lottos:
        if k == 0:
            question += 1
    good = 7 - (count + question)
    if count == 0:
        bad = 6
        if question == 0:
            good = 6
    else:
        bad = 7 - count

    answer.append(good)
    answer.append(bad)

    return answer