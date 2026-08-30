#스택을 이용해서 '('를 넣다가 ')'를 만나면 pop()시키기
#첫번째부터 )이거나, 리스트에 남아있는게 있음 false

#from collections import deque

def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:              # c == ')'
            if not stack:  # 닫을 게 없는데 ) 나옴 (len(stack) == 0)
                return False
            stack.pop()
    return not stack       # 다 끝나고 비었으면 True

solution("(())")
