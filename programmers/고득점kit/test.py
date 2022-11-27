def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        tmp = sum(a)
        for j in range(2, tmp):
            if tmp % j == 0:
                break
        else:
            answer += 1
    print(answer)
    return answer

solution([1,2,3,4])