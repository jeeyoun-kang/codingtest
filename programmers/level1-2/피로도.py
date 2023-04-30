#유저가 탐험할수 있는 최대 던전 수 구하기
#던전을 도는 순서에 따라 갈수 있는 신전의 개수가 달라질 수 있다.
from itertools import permutations as pm
def solution(k, dungeons): #현재피로도,[최소,소모피로도 2차원배열]
    answer=0
    for pm_result in pm(dungeons,len(dungeons)):
        tmp=k
        cnt=0
        for min_stat,minus in pm_result:
            if tmp>=min_stat:
                tmp-=minus
                cnt+=1
        answer=max(answer,cnt)
    return answer




