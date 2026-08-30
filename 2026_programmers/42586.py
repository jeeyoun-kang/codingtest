#뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
#작업의 진도가 적힌 정수 배열 progresses
#각 작업의 개발 속도가 적힌 정수 배열 speeds
#각 배포마다 몇 개의 기능이 배포

from collections import deque


def solution(progresses, speeds):
    answer = []
    remain = []
    for i in range(len(progresses)):
        if((100-progresses[i])%speeds[i]) == 0:
            remain.append((100-progresses[i])//speeds[i])
        else:
            remain.append((100-progresses[i])//speeds[i] + 1)
    q = deque(remain)

    while q: #언뜻 while/while문이여서 O(n^2)처럼 보이지만 실제로 첫 while문은 O(1)이여서 총 O(n)
        front = q.popleft()
        cnt = 1
        while q and q[0] <= front:
            q.popleft()
            cnt+=1
        answer.append(cnt)
    print(answer)
    return answer

solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])