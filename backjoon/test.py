from collections import deque

queue = deque([1,2])
x,y = queue.popleft()
print(x,y)