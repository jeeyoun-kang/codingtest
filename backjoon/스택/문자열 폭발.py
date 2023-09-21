#단순 구현시 시간초과 -> stack으로 해결
import sys
input = sys.stdin.readline

c= list(input().rstrip())
bomb = list(input().rstrip())
stack = []

for i in range(len(c)):
    stack.append(c[i])
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")


    