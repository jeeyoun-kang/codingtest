#이분탐색유형
#while문의 시간복잡도는 O(logn)이다.
#출력해야 하는 두 용액은 특성값의 오름차순으로 출력
#정답이 두개 이상일 경우 그 중 하나만 출력(스페셜저지)
import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int,input().split()))

left, right = 0, n-1 #시작점과 끝점을 정함
temp = 2000000000
a, b = 0, 0
while left < right:
    result = liquid[left]+liquid[right]

    if abs(result)< temp:
        a,b = liquid[left],liquid[right]
        temp = abs(result)

    if result<0 :
        left += 1
    else:
        right -= 1

print(a,b)