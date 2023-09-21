#문자열의 뒤에 A를 추가한다.
#문자열을 뒤집고 뒤에 B를 추가한다.
#주어진 조건으로 s->t로 만들시 1 , 아니면 0을 출력
import sys
input = sys.stdin.readline
from collections import deque
s = input().rstrip()
t = input().rstrip()
queue = deque([s])
while queue:
    v = queue.popleft()
    if v==t:
        print(1)
        break
    if len(v)>len(t):
        print(0)
        break
    #1번조건
    test1 = v+'A'
    #2번
    list_v = list(v)
    list_v.reverse()
    list_v.append('B')
    test2="".join(list_v)
    queue.append(test1)
    queue.append(test2)

#시간 초과가 나서 t->s로 바꾸는 법으로 고침!
S = list(map(str, input()))
T = list(map(str, input()))

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)

