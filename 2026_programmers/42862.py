#학생수, 잃어버린 학생리스트, 여벌존재하는 학생리스트
#바로 앞/뒤 학생기준으로만 빌리기 가능
# 도둑맞았는데 여벌도 있는애는 자기자신만 입기 가능하니 제외(line7~8)
from collections import deque

def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)      # lost기준 교집합 빼기
    reserve_set = set(reserve) - set(lost)   # reserve기준 교집합 빼기
    lost = sorted(lost_set)
    rev = deque(sorted(reserve_set))
    answer = n - len(lost)
    while rev:
        q = rev.popleft()
        for i in range(len(lost)):
            if lost[i] == q-1 or lost[i] == q+1:
                answer += 1
                lost.pop(i)
                break
    return answer

solution(5,[2,4],[1,3,5])