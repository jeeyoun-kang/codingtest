# from itertools import permutations as pm
#
#
# def solution(numbers):
#     test = []
#     for i in pm(numbers, len(numbers)):
#         result = ''.join(map(str, list(i)))
#         print(result)
#         test.append(result)
#
#     return max(test)
# 단순 순열로 풀었을때 시간초과
#람다함수를 이용해 문자열비교(아스키코드로 비교해 각 인덱스끼리 비교 가능)
def solution(numbers):
    numbers = list(map(str, numbers))
    #문자열 비교는 첫번째 문자를 아스키코드로 비교, 같을때는 두번째 문자값 비교
    numbers.sort(key=lambda x : x*3,reverse=True)
    return str(int(''.join(numbers)))
