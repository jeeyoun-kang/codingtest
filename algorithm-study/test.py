# K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력
import time
start_time = time.time() # 측정 시작


import sys
input = sys.stdin.readline
n,k= map(int,input().split())
number =list(input().strip())
count=0
result=0
#맨앞부분을 기준으로 정리
for i in range(2,n+2):
    count+=1
    if number[0]<number[i-1]:
        result=max(result,int(number[i-1]))
    if result>=int(number[i]): #max값이 바로 다음 값보다 클때
        break

for j in range(count):
    number.pop(0)
findmin=list(number)
findmin.sort() #최솟값 두개를 찾기위한 리스트 정렬

for i in range(k-count):
    if number.index(findmin[0])<number.index(findmin[1]):
        number.pop(number.index(findmin[0]))
        findmin.pop(0)
    else:
        number.pop(number.index(findmin[1]))
        findmin.pop(1)
print("".join(number))
# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력