import time
start_time = time.time() # 측정 시작
import sys
input = sys.stdin.readline
villiage = []
all_people = 0
N = int(input())
for i in range(N):
    n_viliage, people = map(int, input().split())
    villiage.append([n_viliage, people])
    all_people += people

villiage.sort(key= lambda x: x[0])
count = 0
for i in range(N):
    count += villiage[i] [1]
    if count >= all_people/2:
        print (villiage[i][0])
        break
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
