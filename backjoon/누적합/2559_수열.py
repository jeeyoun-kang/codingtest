#매일 측정한 온도가 정수의 수열로 주어졌을 때,
# 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산

n,k = map(int,input().split()) #일수,연속일
temp=list(map(int,input().split()))
result=[]
total=0
for l in range(k):
    total+=temp[l]
result.append(total)
for i in range(k,n):
    total+=temp[i]
    total = total-temp[i-k]
    result.append(total)
print(max(result))

