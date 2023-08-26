import sys
input = sys.stdin.readline

n = int(input())  # 집 개수
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    #각 RGB값에 대해서 현재 색을 제외한 이전값들의 최솟값 구한뒤 현재 색 더하기
    arr[i][0]+=min(arr[i-1][1],arr[i-1][2])
    arr[i][1]+=min(arr[i-1][0],arr[i-1][2])
    arr[i][2]+=min(arr[i-1][0],arr[i-1][1])
print(min(arr[n-1]))
