from collections import deque
def solution(progresses, speeds):
    answer=[]
    day =deque()
    for i in range(len(progresses)):
        a = 100-progresses[i]
        if a%speeds[i]!=0:
            tmp = a/speeds[i]+1
        else:
            tmp = a/speeds[i]
        day.append(tmp)
    while day:
        v = day.popleft()
        cnt = 1
        while day and v >=day[0]:
            day.popleft()
            cnt+=1
        answer.append(cnt)
    return answer