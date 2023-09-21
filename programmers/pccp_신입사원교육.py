import heapq


# 2명을 선발해 교육
# 교육 후 모든 신입사원들의 능력치의 합의 최솟값을 return
def solution(ability, number):  # 능력치,교육횟수
    heapq.heapify(ability)
    for i in range(number):
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)
        heapq.heappush(ability, a + b)
        heapq.heappush(ability, a + b)

    return sum(ability)

print(solution([10,3,7,2],2))
