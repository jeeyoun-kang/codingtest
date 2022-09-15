# n명모험가
# 공포도 측정
# 공포도 높은모험가-> 대처능력저하
# 동빈이는 공포도 x인 모험가는 반드시 x명이상 구성한 그룹에 참여해야 여행 떠나도록 규정
# n명 모험가 정보 주어질때 , 여행 떠날수있는 그룹수 최댓값
# 3명 , 2,5,4
n = int(input())
data = list(map(int,input().split()))
data.sort() # 오름차순 정렬 data.sort(reverse=True) 내림차순 정렬

result = 0 # 총 그룹수
count = 0 # 현재 그룹에 있는 모험가 수

for i in data :
    count += 1 #현 그룹에 모험가 포함시키기
    if count >= i:
        result += 1
        count = 0


