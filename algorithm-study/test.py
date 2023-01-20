#기프티콘 n개중 기한 가장 적게 남은 기프티콘만 사용가능
#기프티콘 기한 연장을 최소한으로 하고 싶어함
#최소횟수로 기한 연장하면서 기프티콘 다쓰게(기한맞춰서 기프티콘쓰게해야함)

import sys
import math
input=sys.stdin.readline
n=int(input())
deadline=list(map(int,input().split()))
plan=list(map(int,input().split()))
test=0
count = 0
for k in range(n): #연장일보다 기한일 늘리게 함

    if deadline[k]<plan[k]: #기한연장해야되는 기프티콘이 있는경우
        test=(int(plan[k])-int(deadline[k]))//30
        deadline[k]=30*(test + 1)+deadline[k]
        count += test + 1

print(deadline)

#사용할 날짜 비교하면서 더 연장할 기프티콘은 연장하기(수정하기)-스택이용해보기
for j in range(n):
    minplan = plan.index(min(plan))
    mindead = deadline.index(min(deadline))
    if mindead!=minplan:
        deadline[mindead] =30+deadline[mindead]
        count+=1
        print(deadline)
print(count)

if min(plan)==sum(plan)/n:
    count-=math.ceil(count/2)
print(count)