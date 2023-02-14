#당첨확률이 가장 높은걸 사되 같은 확률의 복권들이 있을때 당첨 금액이 높은 복권 사기
#당첨자수=>구매한수 -> 구매한 사람 모두 당첨
#당첨자수<구매한수->무작위로 당첨자 정해짐
# def solution(lotteries):
#     percent=[]
#     result=0
#     for i in range(len(lotteries)):
#         percent.append(lotteries[i][0]/(lotteries[i][1]+1))
#     result
#
#     return answer
#
# #각 복권의 당첨자수, 구매한 사람수,당첨금액
# print([100,100,500],[1000,1000,100])
lotteries=[10,19,800],[20,39,200],[100,199,500]
percent=[]
result=0
result2=[]
for i in range(len(lotteries)):
    percent.append(lotteries[i][0]/(lotteries[i][1]+1))
result=percent.index(max(percent))
if percent.count(max(percent))>=2: #같은 확률 가진경우 2개이상일때
    result=0
    for j in range(len(lotteries)):
        if max(percent)==lotteries[j][0]/(lotteries[j][1]+1):
            result2.append(j)   #0,1
            result=max(result,lotteries[j][2])
    for k in range(len(lotteries)):
        if result==lotteries[k][2]:
            print(k+1)
else:
    print(result+1)