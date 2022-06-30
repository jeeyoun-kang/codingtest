import numpy as np

def solution(arr1, arr2):
    # for i in range(len(arr1)) :
    #     for j in range(len(arr1[i])) :
    #         arr1[i][j]+=arr2[i][j]
    # return arr1
    A = np.array(arr1)
    B = np.array(arr2)
    answer = A+B
    return answer.tolist() #tolist는 array->list형태로 변환
    #파이썬은 array를 지원안하고 list만 지원, numpy를 써서 array를 쓴다.

