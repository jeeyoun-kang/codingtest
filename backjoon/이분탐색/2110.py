import sys
input = sys.stdin.readline
#C개의 공유기를 N개의 집에 적당히 설치해서
# 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램

n,c = map(int,input().split()) #집의개수,공유기개수
house=[]
for i in range(n):
    house.append(int(input()))
house.sort()

#c-2개의 공유기를 가장 먼 위치에 위치하고, 안쪽에서 2개의 간격의 경우의 수를 모두 구한다.
#집들간 최소거리와 최대 거리의 중앙을 mid로 설정!
#mid를 기준으로 현재에서 다음 집 간격이 mid를 초과시 공유기 설치가능
start=1
end=house[-1]-house[0]
answer=0
while start<=end:
    mid = (start + end) // 2
    current=house[0]
    count=1

    for i in range(1,len(house)):
        if house[i]>=current+mid:
            count+=1
            current=house[i]
    if count>=c:
        start=mid+1
        answer = mid
    else:
        end=mid-1
print(answer)