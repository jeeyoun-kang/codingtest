import sys
input = sys.stdin.readline

N = int(input()) ; Dic = [0] * (1+N)
for i in range(1, 1+N) :
    a, b, c = map(int,input().split()) ; Dic[a] = (b, c)

D = [] ; D.append(1) ; Ans = 2*(N-1)
while D :
    n = D.pop() ; a, b = Dic[n]
    if b != -1 : D.append(b)
    Ans -= 1

print(Ans+1)