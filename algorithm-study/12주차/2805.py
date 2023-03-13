# 적어도 M미터의 나무를 집에 가져가기 위해서
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
from bisect import bisect_left
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
trees = list(map(int,input().split()))
result_cnt = 0
#절단기보다 높은 나무들의 윗부분을 가져갈수 있음

trees.sort()
result = 2000000001
#정렬 후 사잇값에 절단기가 리스트 사이에 들어갔을때
# 연산으로 절단기의 높이 최대값 구하기
for k in range(n):
    cnt=0
    tree_index = bisect_left(trees,trees[k])
    for j in range(tree_index,n):
        cnt+=trees[j] - trees[tree_index]
    if cnt>=m:
        result = min(result,cnt)
        result_index = tree_index
if result>m:
    for z in range(result_index+1,n):
        result_cnt += trees[z]
    result = (result_cnt-m)//(n-(result_index+1))
    print(result)


else:
    print(trees[result_index])

