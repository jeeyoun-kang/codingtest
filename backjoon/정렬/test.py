#괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램
# 5자리보다 많이 연속되는 숫자는 없다
#-를 기준으로 괄호 만들기
a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)