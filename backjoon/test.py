import sys
import time
start_time = time.time()
input = sys.stdin.readline
n = int(input())
result = []


# 특정 숫자 x가 소수인지 판별하는 가장 기본적인 알고리즘
def primenumber(x):
    if x == "1":
        return False
    for i in range(2, int(x)):  # 2부터 x-1까지의 모든 숫자
        if int(x) % i == 0:  # 나눠떨어지는게 하나라도 있으면 False
            return False
    return 1  # 전부 나눠떨어지지 않으면 True


for j in range(10 ** (n - 1), 10 ** n):
    j = str(j)
    cnt = 0
    for k in range(n, 0, -1):
        cnt += primenumber(j[:k])
        if cnt == n:
            print(j)
print(time.time()-start_time)