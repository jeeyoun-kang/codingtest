import sys
input = sys.stdin.readline
n = input().rstrip()
result = [] # 모든 최종 값들을 넣을 배열
cnt=0

for j in range(len(n)):
    if int(n[j])%2!=0:
        cnt+=1
def three(n):
    for i in range(int(n) - 1):
        for k in range(i, int(n) - 2):
            n = int(n[:i]) + int(n[i + 1:k]) + int(n[:k])
            return n
while len(result)!=6:
    if len(n)>3: #네자리 이상일때
        n = three(n)
        n = str(n)
    elif len(n)==3:
        if int(n[0])%2!=0:
            cnt+=1
        if int(n[1])%2!=0:
            cnt+=1
        if int(n[2])%2!=0:
            cnt+=1
        n=int(n[0])+int(n[1])+int(n[2])
        n = str(n)
    elif len(n)==2:
        if int(n[0])%2!=0:
            cnt+=1
        if int(n[1]) %2!=0:
            cnt+=1
        n=int(n[0])+int(n[1])
        n = str(n)
    else:
        result.append(cnt)
        cnt=0
print(max(result),min(result))

