import time
import time
start_time = time.time() # 측정 시작

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = input().rstrip()
stack = []
for number in numbers:
    while stack and stack[-1] < number and k > 0:
        stack.pop()
        k -= 1
    stack.append(number)
if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
