
#DFS
#숫자를 하나씩 +/-로 갈라서 마지막에 target이면 1를 리턴에 위로 더해 올림

def solution(numbers, target):

    def dfs(index, sum):
        if(index == len(numbers)):
            if sum == target:
                return 1
            else :
                return 0
        return dfs(index+1,sum+numbers[index]) + dfs(index+1, sum-numbers[index])
    return dfs(0,0) 

solution([1,1,1,1,1],3)

#BFS
# 숫자 하나씩 처리하면서 가능한 합을 큐에 계속 펼쳐면서, 다 끝난뒤, 큐에서 target에 맞는 갯수 카운팅

from collections import deque

def dfs_solution(numbers, target):
    queue = deque([0])                # 현재까지 가능한 합들
    for n in numbers:
        for _ in range(len(queue)):
            cur = queue.popleft()
            queue.append(cur + n)     # 더한 경우
            queue.append(cur - n)     # 뺀 경우
    return list(queue).count(target)  # 최종 합들 중 target 개수

dfs_solution([1,1,1,1,1],3)

#모든 부호 조합 만든뒤, target 카운팅
#zip은 for문에 여러 리스트 담아서 뿌릴수있게 구현하는 함수

from itertools import product

def prod_solution(numbers, target):
    answer = 0                                          # ① 카운터 준비
    for signs in product((1, -1), repeat=len(numbers)): #  원소 수 만큼 부호 조합(부호 수^원소 수)
        total = 0                                       # ③ 이번 조합 합 계산
        for n, s in zip(numbers, signs):
            total += n * s                              # 원소*부호 합산
        if total == target:                             # ④ target이면 세기
            answer += 1
    return answer      

prod_solution([1,1,1,1,1],3)

