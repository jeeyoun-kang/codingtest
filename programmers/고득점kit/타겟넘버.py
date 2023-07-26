from itertools import combinations as cb

def solution(numbers, target):
    numbers.sort()
    # n개의 음이 아닌 정수
    # 순서는 바꾸지 않고 +/-로 타켓넘버
    total = sum(numbers)
    ex = total-target # 빼야되는 수
    print(ex) # -ex/2인 값이나 합을 더해주면 된다
    cnt=0
    #-의 개수 - 순열
    for i in range(len(numbers)):
        for number in cb(numbers,i+1):
            if sum(list(number))==ex/2:
                cnt+=1
    return cnt

#bfs 트리로 모든 경우의수를 구해 타켓넘버에 해당되는 값을 뽑기
# numbers=[1,1,1,1,1]
# target=3
# super = [0]
# for i in numbers:
#     sub=[]
#     for j in super:
#         sub.append(j+i)
#         sub.append(j-i)
#     super=sub
# print(super.count(target))