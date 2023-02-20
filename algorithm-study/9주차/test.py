#수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
#큰 값이 작은 값 찾는 방식
cnt=0
result=[]

if n<k:
    result.append(k)
    while(n!=k):
        if n>k:
            k=k+1
        elif k%2==0:
            k=k//2
        else:
            k=k-1
        cnt += 1
        result.append(k)
elif n>k:
    result.append(n)
    while (n != k):
        if k > n:
            n=n+1
        elif n % 2 == 0:
            n = n // 2
        else:
            n=n-1
        cnt += 1
        result.append(n)
else:
    result.append(n)
print(cnt)
if n<k:
    print(" ".join(map(str,result[::-1])))
else:
    print(" ".join(map(str, result)))

