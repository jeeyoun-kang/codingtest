# import sys
# input = sys.stdin.readline
# n= int(input())
# left=[]
# right=[]
# cnt=0
# numbers = list(map(int,input().split()))
# if numbers.count(max(numbers))==1:
#     for i in range(numbers.index(max(numbers))+1):
#         left.append(numbers[i])
#     for j in range(numbers.index(max(numbers)),n):
#         right.append(numbers[j])
#     print(abs(len(left)-len(right)))
# else:
#     for i in range(numbers.index(max(numbers))):
#         left.append(numbers[i])
#     for j in range(numbers.index(max(numbers)),n):
#         right.append(numbers[j])
#     print(abs(len(left)-len(right)))

n = int(input())
seq = list(map(int, input().split()))

dp = [[0]*(n+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if seq[-i]==seq[j-1] : dp[i][j] = dp[i-1][j-1]+1
        else : dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(n-dp[n][n])