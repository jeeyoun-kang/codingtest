
# part : 선수 이름 배열, copm : 완주선수 배열
# 완주못한 선수 리턴
# 동명이인이 존재가능성 > set, in 못씀 > 반드시 카운팅 : dict, Counter

def solution(participant, completion):

    dict = {}
    for idx,val in enumerate(participant):
        dict[val] = dict.get(val,0)+1
    
    for val in completion:
        dict[val] -=1
    
    for i in dict:
        if dict[i] > 0:
            return i

#Counter 이용

import collectoins

def solution_Counter(participant, completion):

    answer = collectoins.Counter(participant) - collectoins.Counter(completion)
    return list(answer.keys())[0]
    